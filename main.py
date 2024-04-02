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
import click
from terminaltables import SingleTable
from datetime import datetime



DB_NAME = 'tasks.db'

def create_table():
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


@click.group()
@click.version_option(version='0.1', prog_name='Taskmaster')

def main():
    """
    Main function to execute the Taskmaster CLI.
    """
    create_table()


@main.command()
@click.option('--title', '-tl', prompt=True,
               help='Title for the task. [required]')
@click.option('--description', '-de', prompt=False, 
              help='Description for the task. [optional]')
@click.option('--priority', '-pr', prompt=True, default=0,
              help='Priority for the task (0 - 5). [required]. default=0')
@click.option('--due_date', '-dd', prompt=False, default=None,
              help='Due date for the task. [optional]')

def add_task(title, description, priority, due_date):
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

    user_data = [
        ['Task Information', 'Details'],
        ['Task Title', title],
        ['Task Description', description],
        ['Task Priority', priority],
        ['Task Due Date', due_date],
    ]

    tbl = SingleTable(user_data)
    click.echo(tbl.table)

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
            INSERT INTO tasks (title, description, due_date, priority, created_at, updated_at) 
            VALUES (?, ?, ?, ?, ?, ?)""", (title, description, due_date, priority, datetime.now(), datetime.now(),))
    conn.commit()
    conn.close()
    click.secho('Add Task successfully', fg='green')

if __name__ == '__main__':
    main()
