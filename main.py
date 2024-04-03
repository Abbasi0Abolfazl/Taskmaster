"""
Taskmaster

This CLI tool allows users to efficiently manage their to-do lists from the command line.
Users can add, remove, list, and update tasks using simple commands.
The tasks are stored in a SQLite database named 'tasks.db' in the same directory as the script.

Commands:
  - add: Add a new task to the to-do list.
  - remove: Remove a task from the to-do list by its ID.
  - list: List all tasks currently in the to-do list.
  - update: Update the task with the specified ID to a new task.

Usage:
  taskmaster add <task>: Add a new task.
  taskmaster remove <task_id>: Remove the task with the specified ID.
  taskmaster list: List all tasks.
  taskmaster update <task_id> <new_task>: Update the task with the specified ID to a new task.
"""

import sqlite3
from datetime import datetime
import click
from terminaltables import SingleTable



DB_NAME = 'tasks.db'

def create_table() -> None:
    """create DB and tasks table"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
            CREATE TABLE IF NOT EXISTS "tasks" (
                "id"	INTEGER,
                "title"	TEXT NOT NULL,
                "description"	TEXT,
                "due_date"	TIMESTAMP,
                "priority"	INTEGER DEFAULT 0,
                "created_at"	TIMESTAMP,
                "updated_at"	TIMESTAMP,
                PRIMARY KEY("id")
            );''')
    conn.commit()
    conn.close()


def insert_task(title: str, description: str, priority: int, due_date: str) -> None:
    """Insert a new task into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
            INSERT INTO tasks (title, description, due_date, priority, created_at, updated_at) 
            VALUES (?, ?, ?, ?, ?, ?)""", 
            (title, description, due_date, priority, datetime.now(), datetime.now()))
    conn.commit()
    conn.close()


def select_all_tasks() -> list:
    """
    Retrieve all tasks from the database.

    Returns:
        list of tuples: List of tuples representing all tasks in the database.
    """
    tasks = []
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()
    except sqlite3.Error as e:
        print("Error retrieving tasks:", e)
    return tasks


def delete_task(task_id: int) -> None:
    """
    Delete a task from the database.

    Args:
        task_id (int): The ID of the task to be deleted.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Check if task ID exists
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        task = cursor.fetchone()
        
        if task:
            # Task exists, proceed with deletion
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
            conn.close()
            click.secho('Task deleted successfully', fg='green')
        else:
            # Task doesn't exist
            click.secho('Task ID does not exist', fg='red')
    except sqlite3.Error as e:
        print("Error deleting task:", e)



@click.group()
@click.version_option(version='0.1', prog_name='Taskmaster')

def main():
    """
    Taskmaster - Manage your to-do list from the command line.
    """
    create_table()


def validate_due_date(due_date: str) -> bool:
    """
    Validate the due date format.

    Args:
        due_date (str): The due date string.

    Returns:
        bool: True if the due date format is valid, False otherwise.
    """
    try:
        if due_date:
            datetime.strptime(due_date, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    

@main.command()
@click.option('--title', '-tl', prompt=True,
               help='Title for the task. [required]')
@click.option('--description', '-de', prompt=False, 
              help='Description for the task. [optional]')
@click.option('--priority', '-pr', prompt=True, default=0,
              help='Priority for the task (0 - 5). [required]. default=0')
@click.option('--due_date', '-dd', prompt=False, default=None,
              help='Due date for the task. [optional]')

def add(title: str, description: str, priority: int, due_date: str) -> None:
    """
    Add a new task.

    This command allows users to add a new task to the to-do list.
    The user is prompted to enter the title of the task, and optionally, a description, priority, and due date.
    The task is then added to the list and displayed in a table format, along with the provided information.

    Args:
        title (str): The title of the task.
        description (str, optional): The description of the task (optional).
        priority (int): The priority of the task.
        due_date (str, optional): The due date of the task (optional).

    Example:
        taskmaster add-task --title "Finish project" --description "Complete the final report" --priority 1 --due_date "2024-04-10"
        
    """

    if due_date and not validate_due_date(due_date):
        click.secho('[!] Invalid due date format. Please use YYYY-MM-DD format.', fg='red')
        return

    user_data = [
        ['Task Information', 'Details'],
        ['Task Title', title],
        ['Task Description', description],
        ['Task Priority', priority],
        ['Task Due Date', due_date],
    ]

    # Create SingleTable instance
    tbl = SingleTable(user_data)
    click.echo(tbl.table)   
    insert_task(title, description, priority, due_date)
    click.secho('Add Task successfully', fg='green')


@main.command() 
def show() -> None:
    """
    Show all tasks.

    This function retrieves all tasks from the database and displays them in a tabular format.
    """

    all_tasks = select_all_tasks()

    # Prepare data for SingleTable
    table_data = [
        ('ID', 'Title', 'Description', 'Priority', 'Due Date', 'Created At', 'Updated At')
        ]
    table_data.extend(all_tasks)

    # Create SingleTable instance
    tbl = SingleTable(table_data)
    click.echo(tbl.table)


@main.command()
@click.option('--task_id', '-id', prompt=True, type=int,
              help='ID of the task to be deleted. [required]')
def delete(task_id: int) -> None:
    """
    Delete a task by its ID.

    This command allows users to delete a task from the to-do list by specifying its ID.

    Args:
        task_id (int): The ID of the task to be deleted.
    """
    delete_task(task_id)


if __name__ == '__main__':
    main()
