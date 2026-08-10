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
    """Resolve a list-of-keys path to (container, last_key)."""
    cur = doc
    for key in path[:-1]:
        if key not in cur:
            if not create:
                raise KeyError(f"path not found: {'/'.join(map(str, path))}")
            cur[key] = {}
        cur = cur[key]
    return cur, path[-1]


def op_set(doc, entry):
    container, key = _walk(doc, entry["path"], create=True)
    container[key] = entry["value"]


def op_remove(doc, entry):
    container, key = _walk(doc, entry["path"])
    container.pop(key, None)


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


TRANSFORMS = {
    "strip_auth_param": t_strip_auth_param,
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
