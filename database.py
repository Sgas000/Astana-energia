import sqlite3

def get_connection():
    conn = sqlite3.connect("tech_tasks.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        equipment_type TEXT NOT NULL,
        status TEXT NOT NULL,
        technician TEXT NOT NULL,
        date TEXT NOT NULL,
        description TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()
