from app import app, db, Todo
from datetime import datetime

def seed_database():
    with app.app_context():
        # Clear existing data
        Todo.query.delete()
        
        # Create sample todos
        sample_todos = [
            Todo(
                title="Complete Project Documentation",
                description="Write comprehensive documentation for the todo application including setup instructions and API endpoints",
                completed=False,
                created_at=datetime.utcnow()
            ),
            Todo(
                title="Implement User Authentication",
                description="Add user authentication and authorization to the todo application",
                completed=False,
                created_at=datetime.utcnow()
            ),
            Todo(
                title="Add Task Categories",
                description="Implement task categorization feature to organize todos by different categories",
                completed=True,
                created_at=datetime.utcnow()
            ),
            Todo(
                title="Set Up Unit Tests",
                description="Write unit tests for all API endpoints and database operations",
                completed=False,
                created_at=datetime.utcnow()
            ),
            Todo(
                title="Deploy to Production",
                description="Deploy the todo application to a production environment",
                completed=False,
                created_at=datetime.utcnow()
            )
        ]
        
        # Add todos to database
        for todo in sample_todos:
            db.session.add(todo)
        
        # Commit the changes
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database() 