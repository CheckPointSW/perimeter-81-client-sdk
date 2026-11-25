#!/usr/bin/env python3
"""Build api/swagger.yaml from api/v3.upstream.yaml + api/overlay.yaml.

api/v3.upstream.yaml is pristine vendor output and is never edited.
All corrections live in api/overlay.yaml so they are reviewable and so each
one can be deleted when upstream fixes the underlying defect.
"""
import pathlib, sys, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
UPSTREAM = ROOT / "api" / "v3.upstream.yaml"
OVERLAY = ROOT / "api" / "overlay.yaml"
OUT = ROOT / "api" / "swagger.yaml"

HTTP_METHODS = ("get", "post", "put", "delete", "patch", "head", "options")


def _walk(doc, path, create=False):
    """Resolve a list-of-keys path to (container, last_key).

    An integer path segment indexes into a list, so a path can reach inside
    a composition keyword's array — `[..., oneOf, 0, additionalProperties]`
    addresses the first oneOf branch. Lists are never created implicitly:
    `create` only auto-vivifies missing mapping keys, because an absent list
    index means the spec's shape has changed underneath the entry and
    silently appending would corrupt branch ordering.
    """
    cur = doc
    for key in path[:-1]:
        if isinstance(cur, list):
            if not isinstance(key, int) or not -len(cur) <= key < len(cur):
                raise KeyError(f"path not found: {'/'.join(map(str, path))}")
        elif key not in cur:
            if not create:
                raise KeyError(f"path not found: {'/'.join(map(str, path))}")
            cur[key] = {}
        cur = cur[key]
    return cur, path[-1]


def op_set(doc, entry):
    container, key = _walk(doc, entry["path"], create=True)
    container[key] = entry["value"]


def op_remove(doc, entry):
    """Remove `path`'s last key from its parent container.

    Fails closed by default: if the key is already absent, that means the
    entry's `remove_when` condition has come true (upstream dropped it) or
    the path was wrong to begin with, and either way the entry is now dead —
    it should be caught and deleted, not silently do nothing forever. An
    entry that genuinely needs to tolerate the key already being absent can
    set `optional: true` to opt back into the old pop(key, None) behaviour;
    no entry does today.
    """
    container, key = _walk(doc, entry["path"])
    if key not in container:
        if entry.get("optional"):
            return
        name = entry.get("id", "<unnamed>")
        raise KeyError(
            f"{name}: remove target {'/'.join(map(str, entry['path']))!r} is already "
            f"absent — its remove_when condition may have come true (or the path is "
            f"wrong). Delete this entry, fix the path, or set optional: true if it "
            f"should tolerate absence."
        )
    del container[key]


def op_merge(doc, entry):
    container, key = _walk(doc, entry["path"], create=True)
    target = container.setdefault(key, {})
    if not isinstance(target, dict):
        raise TypeError(f"merge target is not a mapping: {entry['path']}")
    target.update(entry["value"])


def t_strip_auth_param(doc, entry):
    """Remove the per-operation Authorization header parameter.

    v3 declares `Authorization` as an explicit header parameter on every
    operation instead of using securitySchemes. Left in place, openapi-generator
    emits a required .Authorization(string) argument on all 114 methods and the
    SDK's own central bearer injection becomes unreachable.
    """
    removed = 0
    for item in doc["paths"].values():
        for method, op in item.items():
            if method not in HTTP_METHODS or not isinstance(op, dict):
                continue
            params = op.get("parameters")
            if not params:
                continue
            kept = [p for p in params if "authParam" not in str(p.get("$ref", ""))]
            removed += len(params) - len(kept)
            if kept:
                op["parameters"] = kept
            else:
                op.pop("parameters", None)
    doc.get("components", {}).get("parameters", {}).pop("authParam", None)
    print(f"  strip_auth_param: removed {removed} parameter refs")


def _flatten_schema(schema, schemas, depth=0):
    """Resolve $ref/allOf/oneOf/anyOf into a flat {properties, required}
    view. First-declared property/required wins on name conflicts (there
    are none among the schemas this helper is used on)."""
    properties = {}
    required = []

    def visit(node, depth):
        if depth > 8 or not isinstance(node, dict):
            return
        ref = node.get("$ref")
        if ref:
            visit(schemas.get(ref.rsplit("/", 1)[-1]), depth + 1)
            return
        for k, v in (node.get("properties") or {}).items():
            properties.setdefault(k, v)
        for r in node.get("required") or []:
            if r not in required:
                required.append(r)
        for key in ("allOf", "oneOf", "anyOf"):
            for branch in node.get(key) or []:
                visit(branch, depth + 1)

    visit(schema, depth)
    return properties, required


def t_flatten_and_trim_required(doc, entry):
    """Materialize entry["params"]["schema"]'s allOf composition into a flat
    object and replace its required list with entry["params"]["required"].

    Used for schemas whose allOf ancestors are *shared* with a different
    context (typically a create/update request body) that has different
    required-ness than the read-response variant this transform targets.
    Editing the shared ancestor's `required` directly would incorrectly
    change that other context too, so this flattens only the named schema
    in `params`, decoupling it from its ancestors entirely.
    """
    schemas = doc["components"]["schemas"]
    name = entry["params"]["schema"]
    target = schemas[name]
    properties, _ = _flatten_schema(target, schemas)
    required = entry["params"]["required"]
    target.clear()
    target["type"] = "object"
    target["properties"] = properties
    target["required"] = required
    target["additionalProperties"] = True
    print(f"  flatten_and_trim_required: {name} -> required={required}")


TRANSFORMS = {
    "strip_auth_param": t_strip_auth_param,
    "flatten_and_trim_required": t_flatten_and_trim_required,
}

OPS = {"set": op_set, "remove": op_remove, "merge": op_merge}


def main():
    doc = yaml.safe_load(open(UPSTREAM))
    overlay = yaml.safe_load(open(OVERLAY)) or {}
    entries = overlay.get("entries") or []
    for entry in entries:
        name = entry.get("id", "<unnamed>")
        op = entry["op"]
        print(f"applying {name} ({op})")
        if op == "transform":
            TRANSFORMS[entry["transform"]](doc, entry)
        elif op in OPS:
            OPS[op](doc, entry)
        else:
            raise ValueError(f"unknown op {op!r} in entry {name}")
    with open(OUT, "w") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, width=10000, allow_unicode=True)
    print(f"wrote {OUT} ({len(entries)} overlay entries applied)")


if __name__ == "__main__":
    sys.exit(main())
