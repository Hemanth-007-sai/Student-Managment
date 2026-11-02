import sqlite3
from pathlib import Path


DATABASE = Path(__file__).with_name("students.db")


def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_db() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                password TEXT,
                department TEXT NOT NULL
            )
            """
        )
        # Keep an existing Week 7 database usable by adding the Week 8 account fields.
        columns = {
            row[1] for row in connection.execute("PRAGMA table_info(students)")
        }
        if "email" not in columns:
            connection.execute("ALTER TABLE students ADD COLUMN email TEXT")
        if "password" not in columns:
            connection.execute("ALTER TABLE students ADD COLUMN password TEXT")
        connection.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS idx_students_email "
            "ON students(email) WHERE email IS NOT NULL"
        )
