# ============================================================
# Ronaldo Free Kick Analysis — Query Helpers
# ============================================================
# Lightweight wrappers around common DuckDB query patterns.
# Analysis modules use these rather than writing raw SQL inline.
# ============================================================

import pandas as pd
import duckdb
from pipeline.db.connection import get_connection


def query_df(sql: str, conn=None, params: list = None) -> pd.DataFrame:
    """
    Execute a SQL query and return results as a DataFrame.

    Args:
        sql:    SQL string. Use ? for positional parameters.
        conn:   Optional existing connection. Opens one if not provided.
        params: Optional list of positional parameter values.

    Returns:
        pd.DataFrame
    """
    close_after = False
    if conn is None:
        conn = get_connection()
        close_after = True

    try:
        if params:
            result = conn.execute(sql, params).df()
        else:
            result = conn.execute(sql).df()
        return result
    finally:
        if close_after:
            conn.close()


def execute(sql: str, conn=None, params: list = None) -> None:
    """
    Execute a SQL statement with no return value (INSERT, UPDATE, DELETE).

    Args:
        sql:    SQL string. Use ? for positional parameters.
        conn:   Optional existing connection. Opens one if not provided.
        params: Optional list of positional parameter values.
    """
    close_after = False
    if conn is None:
        conn = get_connection()
        close_after = True

    try:
        if params:
            conn.execute(sql, params)
        else:
            conn.execute(sql)
    finally:
        if close_after:
            conn.close()


def insert_df(df: pd.DataFrame, table: str, conn=None) -> int:
    """
    Insert a DataFrame into a table using DuckDB's register + INSERT SELECT.
    Appends rows — does not replace existing data.

    Args:
        df:     DataFrame whose columns match the target table.
        table:  Target table name.
        conn:   Optional existing connection.

    Returns:
        Number of rows inserted.
    """
    close_after = False
    if conn is None:
        conn = get_connection()
        close_after = True

    try:
        conn.register("_insert_df", df)
        conn.execute(f"INSERT INTO {table} SELECT * FROM _insert_df")
        conn.unregister("_insert_df")
        return len(df)
    finally:
        if close_after:
            conn.close()


def upsert_df(df: pd.DataFrame, table: str, key_col: str, conn=None) -> int:
    """
    Upsert a DataFrame into a table using INSERT OR REPLACE.
    Replaces existing rows where key_col matches.

    Args:
        df:      DataFrame whose columns match the target table.
        table:   Target table name.
        key_col: Primary key column name.
        conn:    Optional existing connection.

    Returns:
        Number of rows upserted.
    """
    close_after = False
    if conn is None:
        conn = get_connection()
        close_after = True

    try:
        conn.register("_upsert_df", df)
        conn.execute(f"""
            INSERT OR REPLACE INTO {table}
            SELECT * FROM _upsert_df
        """)
        conn.unregister("_upsert_df")
        return len(df)
    finally:
        if close_after:
            conn.close()


def table_exists(table: str, conn=None) -> bool:
    """Check whether a table exists in the database."""
    close_after = False
    if conn is None:
        conn = get_connection()
        close_after = True

    try:
        result = conn.execute(
            "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = ?",
            [table]
        ).fetchone()
        return result[0] > 0
    finally:
        if close_after:
            conn.close()


def row_count(table: str, conn=None) -> int:
    """Return the number of rows in a table."""
    close_after = False
    if conn is None:
        conn = get_connection()
        close_after = True

    try:
        result = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()
        return result[0]
    finally:
        if close_after:
            conn.close()