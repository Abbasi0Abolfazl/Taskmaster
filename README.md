# Taskmaster
Taskmaster is a Python CLI tool built with Click module for efficient and intuitive management of to-do lists. Empower yourself to become the master of your tasks with Taskmaster. Effortlessly add, remove, update, and track your tasks from the command line. Stay organized, stay productive

It seems like you've provided a detailed guide on how to get started with Taskmaster, a Python CLI tool for managing to-do lists. Here's a breakdown of what you've provided:

### Project Setup
1. **Clone the Repository**: Clone the Taskmaster repository from GitHub.
   ```sh
   git clone git@github.com:Abbasi0Abolfazl/Taskmaster.git
   ```
2. **Navigate to Project Directory**: Change into the Taskmaster project directory.
   ```sh
   cd Taskmaster
   ```

### Setting Up Virtual Environment
- **Linux**:
  ```shell
  python3 -m venv env_dev
  source env_dev/bin/activate
  ```
- **Windows**:
  ```shell
  python -m venv myenv
  myenv\Scripts\activate
  ```

### Installing Required Packages
```sh
python -m pip install -r requirements.txt
```

### Usage
- **Add Task**: Add a new task.
  ```bash
  python taskmaster.py add --title "Finish project" --description "Complete the final report" --priority 1 --due_date <yyyy-mm-dd>
  ```
- **Delete Task**: Delete a task by specifying its ID.
  ```bash
  python taskmaster.py delete -id <task_id>
  ```
- **Show Tasks**: Display all tasks.
  ```bash
  python taskmaster.py show
  ```
- **Update Task**: Update a task by specifying its ID and the updated task description.
  ```bash
  python taskmaster.py --task_id <task_id> --new_title "New Task Title" --new_description "New Task Description" --new_priority 5 --new_due_date <yyyy-mm-dd>
  ```

### Contributions
If users encounter issues or have suggestions for improvements, they are encouraged to contribute. They can do so by:
- Opening an issue to report problems or suggest improvements.
- Forking the repository, making changes, and opening a pull request with the proposed changes.

Constructive input is appreciated.

This guide provides a clear path for users to set up Taskmaster, utilize its features, and contribute to its development.


## Documentation
For more detailed information about Taskmaster, please refer to [documents_taskmaster.md](documents_taskmaster.md).
