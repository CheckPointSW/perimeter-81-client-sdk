import subprocess, sys, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent

def build():
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_spec.py")],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return yaml.safe_load(open(ROOT / "api" / "swagger.yaml"))

def test_bearer_security_scheme_restored():
    d = build()
    assert d["components"]["securitySchemes"]["bearer"] == {
        "type": "http", "scheme": "bearer", "bearerFormat": "JWT",
    }
    assert d["security"] == [{"bearer": []}]

def test_no_operation_declares_the_auth_param():
    d = build()
    offenders = []
    for path, item in d["paths"].items():
        for method, op in item.items():
            if method not in ("get", "post", "put", "delete", "patch"):
                continue
            for prm in op.get("parameters") or []:
                if "authParam" in str(prm.get("$ref", "")):
                    offenders.append(f"{method.upper()} {path}")
    assert offenders == [], offenders

def test_upstream_lacks_the_security_scheme_the_overlay_adds():
    """The upstream spec declares no securitySchemes at all — the key is ABSENT,
    not present-but-empty — and no top-level security. That is the defect A1
    corrects, so asserting it here also proves build_spec.py never mutates the
    upstream file."""
    d = yaml.safe_load(open(ROOT / "api" / "v3.upstream.yaml"))
    assert "securitySchemes" not in d.get("components", {})
    assert "security" not in d
