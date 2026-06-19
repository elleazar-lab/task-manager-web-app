# database.py - SQLite database setup and operations
import sqlite3
from datetime import datetime

DATABASE = 'tasks.db'

def get_db_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Create the tasks table if it doesn't exist"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

def get_all_tasks():
    """Get all tasks from the database"""
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks ORDER BY created_at DESC').fetchall()
    conn.close()
    return tasks

def get_task_by_id(task_id):
    """Get a single task by ID"""
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    conn.close()
    return task

def add_task(description):
    """Add a new task"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (description) VALUES (?)', (description,))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id

def update_task(task_id, description):
    """Update a task's description"""
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET description = ? WHERE id = ?', (description, task_id))
    conn.commit()
    conn.close()

def toggle_task(task_id):
    """Toggle task completion status"""
    conn = get_db_connection()
    task = get_task_by_id(task_id)
    if task:
        new_status = 1 if task['completed'] == 0 else 0
        conn.execute('UPDATE tasks SET completed = ? WHERE id = ?', (new_status, task_id))
        conn.commit()
    conn.close()

def delete_task(task_id):
    """Delete a task"""
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def get_task_stats():
    """Get task statistics"""
    conn = get_db_connection()
    total = conn.execute('SELECT COUNT(*) as count FROM tasks').fetchone()['count']
    completed = conn.execute('SELECT COUNT(*) as count FROM tasks WHERE completed = 1').fetchone()['count']
    active = total - completed
    conn.close()
    return {
        'total': total,
        'completed': completed,
        'active': active
    }

# Initialize database when this file is run directly
if __name__ == '__main__':
    init_db()
