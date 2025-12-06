import json
import random
from datetime import datetime


#Task Class
class Task:
    def __init__(self, title, description):
        self.id = random.randint(100, 999)
        self.title = title
        self.description = description
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at
        }


#Task Manager Class
class TaskManager:
    def __init__(self):
        self.file_name = "tasks.json"
        self.tasks = []
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.file_name, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            print("Error: JSON file is corrupted. Starting with empty task list.")
            self.tasks = []

    def save_to_file(self):
        try:
            with open(self.file_name, "w") as file:
                json.dump(self.tasks, file, indent=4)
        except Exception as e:
            print("Error saving file:", e)

    def add_task(self):
        try:
            title = input("Enter task title: ")
            description = input("Enter task description: ")

            new_task = Task(title, description)
            self.tasks.append(new_task.to_dict())

            print("Task added successfully!")
        except Exception as e:
            print("Error adding task:", e)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\n------ Task List ------")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. ID: {task['id']}")
            print(f"   Title: {task['title']}")
            print(f"   Description: {task['description']}")
            print(f"   Created At: {task['created_at']}")
            print("-------------------------")

    def update_task(self):
        try:
            self.view_tasks()
            task_number = int(input("Enter task number to update: ")) - 1

            if task_number < 0 or task_number >= len(self.tasks):
                print("Invalid task number.")
                return

            new_title = input("Enter new title: ")
            new_description = input("Enter new description: ")

            self.tasks[task_number]["title"] = new_title
            self.tasks[task_number]["description"] = new_description

            print("Task updated successfully!")
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print("Error updating task:", e)

    def delete_task(self):
        try:
            self.view_tasks()
            task_number = int(input("Enter task number to delete: ")) - 1

            if task_number < 0 or task_number >= len(self.tasks):
                print("Invalid task number.")
                return

            deleted_task = self.tasks.pop(task_number)
            print(f"Task '{deleted_task['title']}' deleted successfully!")
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print("Error deleting task:", e)


#Main Program
def main():
    task_manager = TaskManager()

    while True:
        print("\n===== Student Task Tracker =====")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.update_task()
        elif choice == "4":
            task_manager.delete_task()
        elif choice == "5":
            task_manager.save_to_file()
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
