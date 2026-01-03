# src/store.py

from models import Todo

# Private module-level list to store todo items
_todos = []
# Private module-level variable to handle sequential ID generation
_next_id = 1
 
def add_todo(title, description=""):
    """
    Creates a new Todo item and adds it to the in-memory store.

    Args:
        title (str): The title of the todo.
        description (str): The optional description of the todo.

    Returns:
        Todo: The newly created and added todo item.
    """
    global _next_id
    new_todo = Todo(id=_next_id, title=title, description=description)
    _todos.append(new_todo)
    _next_id += 1
    return new_todo

def get_all_todos():
    """
    Retrieves all todo items from the store.

    Returns:
        list[Todo]: A list of all todo items.
    """
    return _todos

def get_todo_by_id(todo_id):
    """
    Retrieves a single todo item by its ID.

    Args:
        todo_id (int): The ID of the todo to retrieve.

    Returns:
        Todo or None: The found todo item, or None if not found.
    """
    for todo in _todos:
        if todo.id == todo_id:
            return todo
    return None

def update_todo(todo_id, title=None, description=None):
    """
    Updates the title and/or description of an existing todo item.

    Args:
        todo_id (int): The ID of the todo to update.
        title (str, optional): The new title. Defaults to None.
        description (str, optional): The new description. Defaults to None.

    Returns:
        Todo or None: The updated todo item, or None if not found.
    """
    todo = get_todo_by_id(todo_id)
    if not todo:
        return None

    if title is not None:
        todo.title = title
    if description is not None:
        todo.description = description
    
    return todo

def delete_todo(todo_id):
    """
    Deletes a todo item from the store by its ID.

    Args:
        todo_id (int): The ID of the todo to delete.

    Returns:
        bool: True if the deletion was successful, False otherwise.
    """
    todo = get_todo_by_id(todo_id)
    if not todo:
        return False
    
    _todos.remove(todo)
    return True

def update_status(todo_id, status):
    """
    Updates the status of a todo item.

    Args:
        todo_id (int): The ID of the todo to update.
        status (str): The new status ("complete" or "incomplete").

    Returns:
        Todo or None: The updated todo item, or None if not found.
    """
    todo = get_todo_by_id(todo_id)
    if not todo:
        return None
    
    todo.status = status
    return todo
