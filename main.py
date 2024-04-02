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

import click
import sqlite3


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
    pass

if __name__ == '__main__':
    main()
