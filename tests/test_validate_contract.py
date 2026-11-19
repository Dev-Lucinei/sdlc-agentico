import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "validate_contract.py"
EXAMPLES = ROOT / ".agents" / "examples"


def run(path: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        capture_output=True,
        text=True,
    )


def test_valid_envelope():
    r = run(EXAMPLES / "envelope-valid.json")
    assert r.returncode == 0, r.stdout + r.stderr


def test_valid_subagent_summary():
    r = run(EXAMPLES / "subagent-summary-valid.json")
    assert r.returncode == 0, r.stdout + r.stderr


def test_invalid_summary():
    r = run(EXAMPLES / "subagent-summary-invalid.json")
    assert r.returncode == 1, r.stdout + r.stderr
    assert "objetivo" in (r.stdout + r.stderr)


def test_missing_file():
    r = run(EXAMPLES / "nope.json")
    assert r.returncode == 1
