from database import get_db_connection


def get_all_tasks():
    connection = get_db_connection()
    tasks = connection.execute("SELECT * FROM tasks").fetchall()
    connection.close()
    return tasks


def get_task_by_id(task_id):
    connection = get_db_connection()
    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()
    connection.close()
    return task


def create_task(title, description, priority, due_date):
    connection = get_db_connection()
    connection.execute(
        """
        INSERT INTO tasks (title, description, priority, due_date, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        (title, description, priority, due_date, "Pending"),
    )
    connection.commit()
    connection.close()


def update_task(task_id, title, description, priority, due_date, status):
    connection = get_db_connection()
    connection.execute(
        """
        UPDATE tasks
        SET title = ?, description = ?, priority = ?, due_date = ?, status = ?
        WHERE id = ?
        """,
        (title, description, priority, due_date, status, task_id),
    )
    connection.commit()
    connection.close()


def delete_task(task_id):
    connection = get_db_connection()
    connection.execute(
        "DELETE FROM tasks WHERE id = ?", (task_id,)
    )
    connection.commit()
    connection.close()
