# ============================================================
# Ronaldo Free Kick Analysis — DuckDB Connection Helper
# ============================================================
# Provides a single connection factory used across the pipeline.
# All modules import get_connection() from here — never open
# a raw duckdb.connect() call elsewhere.
# ============================================================

import os
import duckdb
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Default DB path, overridden by DB_PATH env var
_DEFAULT_DB_PATH = Path(__file__).parent / "ronaldo_freekicks.duckdb"


def get_db_path() -> Path:
    raw = os.getenv("DB_PATH", str(_DEFAULT_DB_PATH))
    path = Path(raw)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def get_connection(read_only: bool = False) -> duckdb.DuckDBPyConnection:
    """
    Return an open DuckDB connection.

    Args:
        read_only: Open in read-only mode (safe for parallel reads).

    Returns:
        duckdb.DuckDBPyConnection
    """
    db_path = get_db_path()
    conn = duckdb.connect(str(db_path), read_only=read_only)
    return conn


def get_in_memory_connection() -> duckdb.DuckDBPyConnection:
    """
    Return an in-memory DuckDB connection.
    Used in tests only — no file is written.
    """
    return duckdb.connect(":memory:")