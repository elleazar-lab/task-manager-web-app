# app.py - Main Flask application
from flask import Flask, render_template, request, jsonify, redirect, url_for
import database

app = Flask(__name__)

# Initialize database on startup
database.init_db()

@app.route('/')
def index():
    """Home page - displays task manager"""
    tasks = database.get_all_tasks()
    stats = database.get_task_stats()
    return render_template('index.html', tasks=tasks, stats=stats)

@app.route('/api/tasks')
def get_tasks():
    """API endpoint to get all tasks (for JavaScript)"""
    tasks = database.get_all_tasks()
    return jsonify([dict(task) for task in tasks])

@app.route('/api/tasks', methods=['POST'])
def add_task():
    """API endpoint to add a new task"""
    data = request.get_json()
    description = data.get('description', '').strip()
    
    if not description:
        return jsonify({'error': 'Description is required'}), 400
    
    task_id = database.add_task(description)
    return jsonify({'id': task_id, 'message': 'Task added successfully'}), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """API endpoint to update a task"""
    data = request.get_json()
    description = data.get('description', '').strip()
    
    if not description:
        return jsonify({'error': 'Description is required'}), 400
    
    task = database.get_task_by_id(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    database.update_task(task_id, description)
    return jsonify({'message': 'Task updated successfully'})

@app.route('/api/tasks/<int:task_id>/toggle', methods=['PUT'])
def toggle_task(task_id):
    """API endpoint to toggle task completion"""
    task = database.get_task_by_id(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    database.toggle_task(task_id)
    return jsonify({'message': 'Task toggled successfully'})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """API endpoint to delete a task"""
    task = database.get_task_by_id(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    database.delete_task(task_id)
    return jsonify({'message': 'Task deleted successfully'})

@app.route('/api/stats')
def get_stats():
    """API endpoint to get task statistics"""
    return jsonify(database.get_task_stats())

if __name__ == '__main__':
    print("=" * 40)
    print("📝 Task Manager Web App")
    print("=" * 40)
    print("Starting web server...")
    print("Open http://127.0.0.1:5000 in your browser")
    print("Press Ctrl+C to stop")
    print("=" * 40)
    app.run(debug=True, host='0.0.0.0', port=5000)
