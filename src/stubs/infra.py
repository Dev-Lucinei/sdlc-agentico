"""Stubs de infraestrutura local (SQLite descartavel + pyproject.toml ficticio)."""

from __future__ import annotations

import os
import sqlite3
import tempfile
import tomllib
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

_DEFAULT_COVERAGE = 50


def _find_real_pyproject(start: Path) -> Path | None:
    """Procura um pyproject.toml real subindo a partir de `start`."""
    current = start.resolve()
    if current.is_file():
        current = current.parent
    for candidate_dir in (current, *current.parents):
        candidate = candidate_dir / "pyproject.toml"
        if candidate.is_file():
            return candidate
    return None


def _read_coverage_threshold(pyproject_path: Path | None) -> int:
    """Le o fail_under do pyproject real; default 50 se ausente/invalido."""
    if pyproject_path is None:
        return _DEFAULT_COVERAGE
    try:
        with pyproject_path.open("rb") as fh:
            data = tomllib.load(fh)
    except (OSError, tomllib.TOMLDecodeError):
        return _DEFAULT_COVERAGE
    report = data.get("tool", {}).get("coverage", {}).get("report", {})
    value = report.get("fail_under", _DEFAULT_COVERAGE)
    try:
        return int(value)
    except (TypeError, ValueError):
        return _DEFAULT_COVERAGE


def _render_stub_pyproject(coverage: int) -> str:
    return f"""# pyproject.toml (stub) - thresholds absolutos (D-V0-01 resolvido)
# cobertura minima >= {coverage}% ; erros criticos = 0

[tool.ruff]
line-length = 100
target-version = "py312"
select = ["E", "F", "W", "I"]

[tool.mypy]
python_version = "3.12"
strict = false
disallow_untyped_defs = true

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra --cov=src --cov-report=term-missing --cov-fail-under={coverage}"
testpaths = ["tests"]

[tool.coverage.run]
source = ["src"]
branch = true

[tool.coverage.report]
fail_under = {coverage}
show_missing = true
"""


# Conteudo padrao (thresholds reais, D-V0-01 resolvido).
STUB_PYPROJECT_CONTENT = _render_stub_pyproject(_DEFAULT_COVERAGE)


class StubDatabase:
    """Banco SQLite descartavel (in-memory por padrao)."""

    def __init__(self, path: str | None = None) -> None:
        self.path = path
        self._conn: sqlite3.Connection | None = None

    def connect(self) -> sqlite3.Connection:
        if self._conn is None:
            if self.path is None:
                self._conn = sqlite3.connect(":memory:")
            else:
                self._conn = sqlite3.connect(self.path)
        return self._conn

    @property
    def connection(self) -> sqlite3.Connection:
        return self.connect()

    def close(self) -> None:
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    def __enter__(self) -> "StubDatabase":
        self.connect()
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


@contextmanager
def create_stub_db(use_file: bool = False) -> Iterator[StubDatabase]:
    """Context manager que cria um banco SQLite descartavel."""
    if use_file:
        fd, path = tempfile.mkstemp(suffix=".sqlite")
        os.close(fd)
        db = StubDatabase(path=path)
        try:
            db.connect()
            yield db
        finally:
            db.close()
            try:
                Path(path).unlink(missing_ok=True)
            except OSError:
                pass
    else:
        db = StubDatabase(path=None)
        try:
            db.connect()
            yield db
        finally:
            db.close()


def write_stub_pyproject(directory: str | Path) -> Path:
    """Escreve um pyproject.toml ficticio com thresholds reais.

    Se existir um pyproject.toml real (procurado a partir de `directory`
    e do local do modulo), le o threshold de cobertura dele em vez de
    usar o valor hardcoded.
    """
    target_dir = Path(directory)
    real = _find_real_pyproject(target_dir)
    if real is None:
        # Fallback: procurar a partir do local deste modulo (raiz do repo).
        real = _find_real_pyproject(Path(__file__).resolve().parent)
    coverage = _read_coverage_threshold(real)
    content = _render_stub_pyproject(coverage)
    target = target_dir / "pyproject.toml"
    target.write_text(content, encoding="utf-8")
    return target


class StubEnvironment:
    """Ambiente local simulado: SQLite descartavel + pyproject.toml ficticio."""

    def __init__(self) -> None:
        self._tmpdir: tempfile.TemporaryDirectory[str] | None = None
        self.root: Path | None = None
        self.db: StubDatabase | None = None

    def __enter__(self) -> "StubEnvironment":
        self._tmpdir = tempfile.TemporaryDirectory()
        self.root = Path(self._tmpdir.name)
        write_stub_pyproject(self.root)
        self.db = StubDatabase(path=None)
        self.db.connect()
        return self

    def __exit__(self, *exc: object) -> None:
        if self.db is not None:
            self.db.close()
        if self._tmpdir is not None:
            self._tmpdir.cleanup()


# Aliases
create_stub_database = create_stub_db
StubSQLite = StubDatabase
create_sqlite_stub = create_stub_db
stub_database = create_stub_db
SQLiteStub = StubDatabase
create_stub_pyproject = write_stub_pyproject
create_pyproject_stub = write_stub_pyproject
write_pyproject_stub = write_stub_pyproject
create_stub_env = StubEnvironment
StubEnv = StubEnvironment
__all__ = [
    "STUB_PYPROJECT_CONTENT",
    "StubDatabase",
    "StubEnvironment",
    "StubSQLite",
    "SQLiteStub",
    "create_stub_db",
    "create_stub_database",
    "create_sqlite_stub",
    "stub_database",
    "write_stub_pyproject",
    "create_stub_pyproject",
    "create_pyproject_stub",
    "write_pyproject_stub",
    "create_stub_env",
    "StubEnv",
]
