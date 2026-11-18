"""Shim de compatibilidade: reexporta src.contract_validator."""

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from src.contract_validator import *  # noqa: F401,F403,E402

if __name__ == "__main__":
    from src.contract_validator import main
    raise SystemExit(main())
