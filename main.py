print("Hello, World!")
print("This is my todo app!")

todos = []

def add_todo(task):
    todos.append(task)
    print(f"Added: {task}")

# Test it
add_todo("Learn Git and GitHub")
print(f"Current todos: {todos}")
