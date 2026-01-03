# Specification: Interactive Todo CLI Application

This document outlines the specifications for a fully interactive, menu-driven command-line interface (CLI) for a todo application.

## 1. Core Principles

- **Interactive and Dynamic**: The application MUST be fully interactive. All actions are initiated through a menu, and all data (e.g., todo titles, descriptions) is provided by the user at runtime via input prompts.
- **Menu-Driven**: The application will present a clear menu of choices to the user, who will select an action to perform. The program flow is determined by these choices.
- **In-Memory Storage**: All todo data is stored in-memory. The data persists only for the duration of the application's session and is lost when the user exits.
- **No Static Data**: There will be no hard-coded or pre-populated todo items. The application starts with an empty list.

## 2. Functional Requirements

### 2.1. Todo Item Structure

A single todo item will have the following structure:
- **id**: An integer, uniquely identifying the todo. Will be generated sequentially starting from 1.
- **title**: A mandatory string representing the task.
- **description**: An optional string for additional details.
- **status**: A string with one of two states: `incomplete` (default) or `complete`.

### 2.2. Application Flow

Upon launch, the application will enter a continuous loop that performs the following steps:
1.  Display the main menu of available actions.
2.  Prompt the user to select an option.
3.  Execute the action corresponding to the user's choice.
4.  After the action is complete, display the menu again.
5.  This loop continues until the user selects the "Exit" option.

### 2.3. Menu Actions

The main menu will provide the following options:

#### 1. **Add a new todo**
- **Interaction**:
    - Prompts the user to enter the `title` for the new todo.
    - Prompts the user to enter a `description` (this is optional; the user can press Enter to skip).
- **Behavior**:
    - Creates a new todo item with a unique, sequential ID.
    - Sets the `status` to `incomplete` by default.
    - Prints a confirmation message, e.g., `Success: Added todo {id}: "{title}"`.

#### 2. **List all todos**
- **Interaction**:
    - The user selects this option from the menu.
- **Behavior**:
    - Prints a formatted list of all existing todo items.
    - The format for each item should be: `{id}. [{status}] - {title}`
    - If no todos exist, it prints a message, e.g., `Info: No todos found.`.

#### 3. **Update a todo**
- **Interaction**:
    - Prompts the user to enter the `id` of the todo to update.
    - If the todo exists, it will prompt the user for a new `title`.
    - It will then prompt the user for a new `description`.
    - The user can press Enter at either prompt to leave the current value unchanged.
- **Behavior**:
    - Finds the todo by its ID.
    - Updates the title and/or description based on user input.
    - If a todo with the given ID is not found, prints an error message, e.g., `Error: Todo with id {id} not found.`.
    - Upon success, prints a confirmation message, e.g., `Success: Updated todo {id}.`.

#### 4. **Delete a todo**
- **Interaction**:
    - Prompts the user to enter the `id` of the todo to delete.
- **Behavior**:
    - Finds the todo by its ID and removes it.
    - If a todo with the given ID is not found, prints an error message, e.g., `Error: Todo with id {id} not found.`.
    - Upon success, prints a confirmation message, e.g., `Success: Deleted todo {id}.`.

#### 5. **Mark a todo as complete**
- **Interaction**:
    - Prompts the user to enter the `id` of the todo to mark as complete.
- **Behavior**:
    - Finds the todo by its ID and sets its `status` to `complete`.
    - If the todo is already complete, it prints an informational message, e.g., `Info: Todo {id} is already marked as complete.`.
    - If a todo with the given ID is not found, prints an error message.
    - Upon success, prints a confirmation message, e.g., `Success: Marked todo {id} as complete.`.

#### 6. **Exit**
- **Interaction**:
    - The user selects this option from the menu.
- **Behavior**:
    - The application terminates, printing a farewell message, e.g., "Exiting application."

## 3. Non-Functional Requirements

- **Error Handling**: The application will handle invalid user input gracefully (e.g., non-numeric input when an ID is expected) and provide clear, user-friendly error messages.
- **Code Style**: Code should be modular and easy to read.
- **Dependencies**: No external libraries should be required to run the application.
- **Platform**: The script will be executed using Python 3.