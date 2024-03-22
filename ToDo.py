#day 3
import json
import atexit
import os

# Initialize task list and completed task count
tasks = []
completed_tasks_count = 0

# Function to save tasks and completed task count to a file
def save_data():
    data = {"tasks": tasks, "completed_tasks_count": completed_tasks_count}
    with open("tasks.json", "w") as f:
        json.dump(data, f)

# Function to load tasks and completed task count from a file
def load_data():
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
            tasks.extend(data.get("tasks", []))
            global completed_tasks_count
            completed_tasks_count = data.get("completed_tasks_count", 0)
    except FileNotFoundError:
        pass

# Register save_data() function to be called when the program exits
atexit.register(save_data)

# Load tasks and completed task count from file when the program starts
load_data()

# Function to add a task
def add_task(task, due_date):
    tasks.append({"task": task, "due_date": due_date})
    save_data()
    print("Task added successfully.")

# Function to view tasks
def view_tasks():
    if tasks:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']} - Due Date: {task['due_date']}")
    else:
        print("No tasks available.")

# Function to complete a task
def complete_task(task_index):
    global completed_tasks_count
    try:
        task = tasks.pop(task_index - 1)
        completed_tasks_count += 1
        save_data()
        print(f"Task '{task['task']}' marked as completed.")
    except IndexError:
        print("Task not found.")

# Function to delete a task
def delete_task(task_index):
    try:
        task = tasks.pop(task_index - 1)
        save_data()
        print(f"Task '{task['task']}' deleted successfully.")
    except IndexError:
        print("Task not found.")

# Function to display available commands
def display_help():
    # Clear the screen by printing empty lines to create space
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-------------------------------")
    print("\nAvailable commands:")
    print("  a/add/+    - Add a new task")
    print("  v/view/?   - View tasks")
    print("  c/complete/= - Mark a task as completed")
    print("  d/delete/r/remove/- - Delete a task")
    print("  help       - Display this help message")
    print("  exit       - Quit the program")
    print("-------------------------------")
    print("\n")

# Main loop
while True:
    command = input("\nEnter command (type 'help' for available commands): ").lower()

    # Clear the screen by printing empty lines to create space
    os.system('cls' if os.name == 'nt' else 'clear')

    if command in ["a", "add", "+"]:
        task = input("Enter task description: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        add_task(task, due_date)
    elif command in ["v", "view", "?"]:
        view_tasks()
    elif command in ["c", "complete", "="]:
        view_tasks()
        try:
            task_index = int(input("Enter the number of the task to mark as completed: "))
            complete_task(task_index)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif command in ["d", "delete", "r", "remove", "-"]:
        view_tasks()
        try:
            task_index = int(input("Enter the number of the task to delete: "))
            delete_task(task_index)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif command == "help":
        display_help()
    elif command == "exit":
        print("Exiting program.")
        break
    else:
        print("Invalid command. Please enter 'help' to see available commands.")

    print(f"Total completed tasks: {completed_tasks_count}")
