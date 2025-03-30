# Todo List Application

A simple CRUD Todo List application built with Python, Flask, and MySQL.

## Setup Instructions

1. Create a MySQL database named `todo_db_python`
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your database credentials:
   ```
   DB_HOST=localhost
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_NAME=todo_db_python
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## API Endpoints

- GET `/todos` - Get all todos
- GET `/todos/<id>` - Get a specific todo
- POST `/todos` - Create a new todo
- PUT `/todos/<id>` - Update a todo
- DELETE `/todos/<id>` - Delete a todo

## Example Request Body

For POST and PUT requests:
```json
{
    "title": "Task title",
    "description": "Task description",
    "completed": false
}
``` 