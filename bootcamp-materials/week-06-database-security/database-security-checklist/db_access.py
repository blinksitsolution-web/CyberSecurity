#!/usr/bin/env python3
"""Local teaching database for Week 6.

Queries use placeholders. The database lives in memory unless you pass a
path. Nothing here connects to a server you do not own.
"""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


def connect(path: str | Path = ":memory:") -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            secret TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS permissions (
            role TEXT NOT NULL,
            action TEXT NOT NULL,
            allowed INTEGER NOT NULL,
            PRIMARY KEY (role, action)
        );
        """
    )
    return conn


def seed_lab(conn: sqlite3.Connection) -> None:
    """Load fictional lab accounts. These secrets are not real credentials."""
    conn.execute("DELETE FROM users")
    conn.execute("DELETE FROM permissions")
    conn.executemany(
        "INSERT INTO users (username, secret) VALUES (?, ?)",
        (
            ("analyst", "lab-secret"),
            ("admin", "other-secret"),
        ),
    )
    conn.executemany(
        "INSERT INTO permissions (role, action, allowed) VALUES (?, ?, ?)",
        (
            ("analyst", "read_ticket", 1),
            ("analyst", "export_all_customers", 0),
            ("analyst", "create_user", 0),
            ("admin", "read_ticket", 1),
            ("admin", "export_all_customers", 0),
            ("admin", "create_user", 1),
            ("dba", "read_ticket", 1),
            ("dba", "export_all_customers", 0),
            ("dba", "create_user", 0),
        ),
    )
    conn.commit()


def authenticate(conn: sqlite3.Connection, username: str, secret: str) -> bool:
    """Check a username and secret. The inputs stay data, not SQL."""
    row = conn.execute(
        "SELECT username FROM users WHERE username = ? AND secret = ?",
        (username, secret),
    ).fetchone()
    return row is not None


def is_allowed(conn: sqlite3.Connection, role: str, action: str) -> bool:
    row = conn.execute(
        "SELECT allowed FROM permissions WHERE role = ? AND action = ?",
        (role, action),
    ).fetchone()
    return bool(row and row["allowed"] == 1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Check one lab permission")
    parser.add_argument("--role", required=True)
    parser.add_argument("--action", required=True)
    args = parser.parse_args()
    conn = connect()
    seed_lab(conn)
    allowed = is_allowed(conn, args.role, args.action)
    print(f"{args.role} {args.action}: {'allow' if allowed else 'deny'}")


if __name__ == "__main__":
    main()
