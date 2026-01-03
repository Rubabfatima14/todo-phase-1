# src/cli.py
import store

def display_menu():
    """Prints the main menu."""
    print("\n--- Todo App Menu ---")
    print("1. Add a new todo")
    print("2. List all todos")
    print("3. Update a todo")
    print("4. Delete a todo")
    print("5. Mark a todo as complete")
    print("6. Exit")
    print("--------------------")

def get_user_choice():
    """
    Gets the user's menu choice.

    Returns:
        str: The user's choice.
    """
    return input("Enter your choice (1-6): ")

def handle_add_todo():
    """Handles the 'add' action."""
    title = input("Enter the title for the new todo: ")
    if not title:
        display_error("Title cannot be empty.")
        return
    description = input("Enter the description (optional): ")
    todo = store.add_todo(title, description)
    display_success(f'Added todo {todo.id}: "{todo.title}"')

def handle_list_todos():
    """Handles the 'list' action."""
    all_todos = store.get_all_todos()
    display_todos(all_todos)

def get_todo_id_from_user():
    """
    Prompts the user for a todo ID and validates it.

    Returns:
        int or None: The validated todo ID, or None if input is invalid.
    """
    try:
        id_str = input("Enter the todo ID: ")
        return int(id_str)
    except ValueError:
        display_error("Invalid ID. Please enter a number.")
        return None

def handle_update_todo():
    """Handles the 'update' action."""
    todo_id = get_todo_id_from_user()
    if todo_id is None:
        return

    todo = store.get_todo_by_id(todo_id)
    if not todo:
        display_error(f"Todo with id {todo_id} not found.")
        return

    new_title = input(f"Enter new title (current: '{todo.title}') or press Enter to keep: ")
    new_description = input(f"Enter new description (current: '{todo.description}') or press Enter to keep: ")

    # Use old values if new ones are empty
    updated_title = new_title if new_title else todo.title
    updated_description = new_description if new_description else todo.description

    updated_todo = store.update_todo(todo_id, updated_title, updated_description)
    if updated_todo:
        display_success(f"Updated todo {todo_id}.")

def handle_delete_todo():
    """Handles the 'delete' action."""
    todo_id = get_todo_id_from_user()
    if todo_id is None:
        return
    
    if store.delete_todo(todo_id):
        display_success(f"Deleted todo {todo_id}.")
    else:
        display_error(f"Todo with id {todo_id} not found.")

def handle_complete_todo():
    """Handles marking a todo as complete."""
    todo_id = get_todo_id_from_user()
    if todo_id is None:
        return
        
    todo = store.get_todo_by_id(todo_id)
    if not todo:
        display_error(f"Todo with id {todo_id} not found.")
        return
    
    if todo.status == "complete":
        display_info(f"Todo {todo_id} is already marked as complete.")
    else:
        store.update_status(todo_id, "complete")
        display_success(f"Marked todo {todo_id} as complete.")

def main_loop():
    """The main application loop."""
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == '1':
            handle_add_todo()
        elif choice == '2':
            handle_list_todos()
        elif choice == '3':
            handle_update_todo()
        elif choice == '4':
            handle_delete_todo()
        elif choice == '5':
            handle_complete_todo()
        elif choice == '6':
            print("Exiting application.")
            break
        else:
            display_error("Invalid choice. Please enter a number between 1 and 6.")

def display_todos(todos):
    """
    Prints a formatted list of todo items.

    Args:
        todos (list[Todo]): A list of todo items to display.
    """
    if not todos:
        display_info("No todos found.")
        return

    print("\n--- Your Todos ---")
    for todo in todos:
        # Status format updated to match the new spec
        print(f"{todo.id}. [{todo.status}] - {todo.title}")
        if todo.description:
            print(f"      {todo.description}")
    print("------------------")

def display_success(message):
    """
    Prints a success message to the console.

    Args:
        message (str): The message to print.
    """
    print(f"Success: {message}")

def display_error(message):
    """
    Prints an error message to the console.

    Args:
        message (str): The message to print.
    """
    print(f"Error: {message}")

def display_info(message):
    """
    Prints an informational message to the console.

    Args:
        message (str): The message to print.
    """
    print(f"Info: {message}")
