# Implementation Plan: Todo Evolution – Phase 1

This document outlines the development plan for the CLI Todo Application based on the approved specification.

## 1. Project Structure

A `src` directory will be created to house the application's source code. The file structure will be as follows:

- `src/`
    - `models.py`: Defines the data structure for a Todo item.
    - `store.py`: Manages the in-memory list of todos, containing all business logic for creation, retrieval, updating, and deletion.
    - `cli.py`: Handles all command-line input and output, including displaying todos and printing messages.
    - `todo.py`: The main entry point for the application. It will parse command-line arguments and delegate tasks to the other modules.

## 2. Task Breakdown

The implementation will be completed in the following order.

### Task 1: Create Directory and Files
- Create the `src/` directory.
- Create the initial empty Python files:
    - `src/models.py`
    - `src/store.py`
    - `src/cli.py`
    - `src/todo.py`

### Task 2: Implement the Data Model (`src/models.py`)
- Define a Python class `Todo` to represent a todo item.
- The class will have attributes for `id` (int), `title` (str), `description` (str), and `status` (str).

### Task 3: Implement the In-Memory Store (`src/store.py`)
- Create a private module-level list `_todos` to store the todo items.
- Create a private module-level variable `_next_id` to handle sequential ID generation.
- Implement the following functions:
    - `add_todo(title, description)`: Creates a `Todo` object and adds it to the list. Returns the newly created todo.
    - `get_all_todos()`: Returns the full list of todos.
    - `get_todo_by_id(todo_id)`: Returns a single todo by its ID, or `None` if not found.
    - `update_todo(todo_id, title, description)`: Updates the title and/or description of an existing todo. Returns the updated todo, or `None` if not found.
    - `delete_todo(todo_id)`: Removes a todo from the list. Returns `True` on success, `False` if not found.
    - `update_status(todo_id, status)`: Updates the status of a todo. Returns the updated todo, or `None` if not found.

### Task 4: Implement the CLI Interface (`src/cli.py`)
- Implement the following functions:
    - `display_todos(todos)`: Iterates through a list of todos and prints them in the format `{id}. [{status}] - {title}`. If the list is empty, it prints an info message.
    - `display_success(message)`: Prints a formatted success message.
    - `display_error(message)`: Prints a formatted error message.
    - `display_info(message)`: Prints a formatted informational message.

### Task 5: Implement the Main Application Logic (`src/todo.py`)
- Import the necessary functions from `store.py` and `cli.py`.
- Use `sys.argv` to parse command-line arguments.
- Create a main function that acts as a dispatcher, calling the appropriate backend functions based on the command (`add`, `list`, `update`, etc.).
- Handle argument validation and call the `display_error` function for any invalid usage.
- Orchestrate the calls between the store and the CLI for a cohesive user experience.
