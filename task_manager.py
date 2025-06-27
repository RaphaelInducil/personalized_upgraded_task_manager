# Add class
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def update(self, title=None, description=None):
        if title:
            self.set_title(title)
        if description:
            self.set_description(description)

    def display(self, index):
        return f"{index}. Title: {self.get_title()}, Description: {self.get_description()}"
    
# Initialize empty list
tasks = []

# Add task list
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append(Task(title, description))
    print("Task added successfully!")

# Task view
def view_tasks():
    if tasks:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            task.display(idx)
            print(f"{idx}. Title: {task['title']}, Description: {task.get_description()}")
    else:
        print("No tasks available.")

# Update task
def update_task():
    view_tasks()
    if tasks:
        task_index = int(input("Enter the index of the task to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_title = input("Enter new title (Press Enter to skip): ")
            new_description = input("Enter new description (Press Enter to skip): ")
            tasks[task_index].update(new_title, new_description)
            print("Task updated successfully!")
        else:
            print("Invalid task index.")
    else:
        print("No tasks available.")

# Function to delete a task
def delete_task():
    view_tasks()
    if tasks:
        task_index = int(input("Enter the index of the task to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Task '{deleted_task.get_title}' deleted successfully!")
        else:
            print("Invalid task index.")
    else:
        print("No tasks available.")
# Nonsense comment for commit update
# Main loop
while True:
    print("\nInteractive Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Select an option (1-5): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting the Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-5).")
