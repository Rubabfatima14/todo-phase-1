# src/models.py

class Todo:
    """
    Represents a single todo item.
    """
    def __init__(self, id, title, description, status="incomplete"):
        """
        Initializes a new Todo item.

        Args:
            id (int): The unique identifier for the todo.
            title (str): The title of the todo.
            description (str): The description of the todo.
            status (str): The status of the todo, e.g., "incomplete" or "complete".
        """
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def __repr__(self):
        """
        Returns a string representation of the Todo item.
        """
        return f"Todo(id={self.id}, title='{self.title}', status='{self.status}')"
