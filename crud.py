from models import Task
from database import get_connection

def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return [Task(**dict(row)) for row in rows]

def add_task(task: Task):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (id, equipment_type, status, technician, date, description)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (task.id, task.equipment_type, task.status, task.technician, str(task.date), task.description))
    conn.commit()
    conn.close()
    return task

def get_task_by_id(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    row = cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    conn.close()
    return Task(**dict(row)) if row else None

def delete_task(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted > 0
