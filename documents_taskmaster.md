# Taskmaster


Commands:
  - add: Add a new task to the to-do list.
  - delete: Remove a task from the to-do list by its ID.
  - show: List all tasks currently in the to-do list.
  - update: Update the task with the specified ID to a new task.


<a id="main.create_table"></a>

#### create\_table

```python
def create_table() -> None
```

create DB and tasks table

<a id="main.insert_task"></a>

#### insert\_task

```python
def insert_task(title: str, description: str, priority: int,
                due_date: str) -> None
```

Insert a new task into the database.

<a id="main.select_all_tasks"></a>

#### select\_all\_tasks

```python
def select_all_tasks() -> list
```

Retrieve all tasks from the database.

**Returns**:

  list of tuples: List of tuples representing all tasks in the database.

<a id="main.delete_task"></a>

#### delete\_task

```python
def delete_task(task_id: int) -> None
```

Delete a task from the database.

**Arguments**:

- `task_id` _int_ - The ID of the task to be deleted.

<a id="main.update_task"></a>

#### update\_task

```python
def update_task(task_id: int, query, parameters) -> None
```

Update a task in the database.

**Arguments**:

- `task_id` _int_ - The ID of the task to be updated.
- `new_title` _str, optional_ - The new title for the task.
- `new_description` _str, optional_ - The new description for the task.
- `new_priority` _int, optional_ - The new priority for the task.
- `new_due_date` _str, optional_ - The new due date for the task.

<a id="main.generate_update_query"></a>

#### generate\_update\_query

```python
def generate_update_query(updates: dict) -> tuple
```

Generate the SQL update query and parameters based on the provided updates.

**Arguments**:

- `updates` _dict_ - Dictionary containing the updates.
  

**Returns**:

- `tuple` - Tuple containing the SQL update query and parameters.

<a id="main.main"></a>

#### main

```python
@click.group()
@click.version_option(version='0.1', prog_name='Taskmaster')
def main()
```

Taskmaster - Manage your to-do list from the command line.

<a id="main.validate_due_date"></a>

#### validate\_due\_date

```python
def validate_due_date(due_date: str) -> bool
```

Validate the due date format.

**Arguments**:

- `due_date` _str_ - The due date string.
  

**Returns**:

- `bool` - True if the due date format is valid, False otherwise.

<a id="main.add"></a>

#### add

```python
@main.command()
@click.option('--title',
              '-tl',
              prompt=True,
              help='Title for the task. [required]')
@click.option('--description',
              '-de',
              prompt=False,
              help='Description for the task. [optional]')
@click.option('--priority',
              '-pr',
              prompt=True,
              default=0,
              help='Priority for the task (0 - 5). [required]. default=0')
@click.option('--due_date',
              '-dd',
              prompt=False,
              default=None,
              help='Due date for the task. [optional]')
def add(title: str, description: str, priority: int, due_date: str) -> None
```

Add a new task.

This command allows users to add a new task to the to-do list.
The user is prompted to enter the title of the task, and optionally, a description, priority, and due date.
The task is then added to the list and displayed in a table format, along with the provided information.

**Arguments**:

- `title` _str_ - The title of the task.
- `description` _str, optional_ - The description of the task (optional).
- `priority` _int_ - The priority of the task.
- `due_date` _str, optional_ - The due date of the task (optional).
  

**Example**:

  taskmaster add-task --title "Finish project" --description "Complete the final report" --priority 1 --due_date "2024-04-10"

<a id="main.show"></a>

#### show

```python
@main.command()
def show() -> None
```

Show all tasks.

This function retrieves all tasks from the database and displays them in a tabular format.

<a id="main.delete"></a>

#### delete

```python
@main.command()
@click.option('--task_id',
              '-id',
              prompt=True,
              type=int,
              help='ID of the task to be deleted. [required]')
def delete(task_id: int) -> None
```

Delete a task by its ID.

This command allows users to delete a task from the to-do list by specifying its ID.

**Arguments**:

- `task_id` _int_ - The ID of the task to be deleted.

<a id="main.update"></a>

#### update

```python
@main.command()
@click.option('--task_id',
              '-id',
              prompt=True,
              type=int,
              help='ID of the task to be updated.')
@click.option('--new_title',
              '-nt',
              prompt=False,
              help='New title for the task.')
@click.option('--new_description',
              '-nd',
              prompt=False,
              default=None,
              help='New description for the task.')
@click.option('--new_priority',
              '-np',
              prompt=False,
              type=int,
              help='New priority for the task (0 - 5).')
@click.option('--new_due_date',
              '-ndd',
              prompt=False,
              default=None,
              help='New due date for the task.')
def update(task_id: int, new_title: str, new_description: str,
           new_priority: int, new_due_date: str) -> None
```

Update a task.

This command allows users to update a task in the to-do list by specifying its ID.
Users can provide new values for the title, description, priority, and due date.

**Arguments**:

- `task_id` _int_ - The ID of the task to be updated.
- `new_title` _str_ - The new title for the task.
- `new_description` _str, optional_ - The new description for the task.
- `new_priority` _int_ - The new priority for the task.
- `new_due_date` _str, optional_ - The new due date for the task.

