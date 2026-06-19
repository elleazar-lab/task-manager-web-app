# Task Manager Web App

A full-stack task management web application built with Flask, SQLite, HTML, CSS, and JavaScript. Create, edit, delete, and filter tasks with real-time updates.

## Features

- Add Tasks - Create new tasks with descriptions
- Complete Tasks - Toggle task completion status
- Edit Tasks - Update task descriptions inline
- Delete Tasks - Remove tasks permanently
- Filter Tasks - View All, Active, or Completed tasks
- Statistics - Real-time task counts (Total, Active, Completed)
- Persistent Storage - SQLite database saves everything

## Technologies

| Category | Technologies |
|----------|--------------|
| Backend | Python, Flask |
| Database | SQLite |
| Frontend | HTML5, CSS3, JavaScript |
| API | RESTful JSON endpoints |

## How It Works

1. Frontend sends requests to Flask API endpoints
2. Flask processes requests and interacts with SQLite database
3. SQLite stores all tasks with descriptions and completion status
4. JavaScript updates the UI in real-time without page reloads

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/task-manager-web-app.git
cd task-manager-web-app

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
