"""Stubs de infraestrutura local (SQLite descartavel + pyproject.toml ficticio)."""

from __future__ import annotations

import os
import sqlite3
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

STUB_PYPROJECT_CONTENT = """# pyproject.toml ficticio (stub) - thresholds absolutos
[tool.ruff]
line-length = 100
target-version = "py311"

[tool.coverage.report]
fail_under = 50
"""


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
    """Escreve um pyproject.toml ficticio com thresholds absolutos."""
    target = Path(directory) / "pyproject.toml"
    target.write_text(STUB_PYPROJECT_CONTENT, encoding="utf-8")
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
