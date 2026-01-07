import sqlite3

DATABASE_NAME = "taskflow.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()
