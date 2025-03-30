-- Create the database
CREATE DATABASE IF NOT EXISTS todo_db_python;

-- Use the database
USE todo_db_python;

-- Drop existing user if exists
DROP USER IF EXISTS 'todo_user'@'localhost';

-- Create a user and grant privileges with mysql_native_password
CREATE USER 'todo_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'maaz';
GRANT ALL PRIVILEGES ON todo_db_python.* TO 'todo_user'@'localhost';
FLUSH PRIVILEGES; 