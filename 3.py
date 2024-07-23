# To-Do List Application

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "pending"})
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task['task']} - {task['status']}")

    def update_task(self, task, new_status):
        for t in self.tasks:
            if t["task"] == task:
                t["status"] = new_status
                print(f"Task '{task}' updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print(f"Task '{task}' deleted successfully!")
                return
        print("Task not found.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            task = input("Enter task: ")
            todo_list.add_task(task)

        elif choice == 2:
            todo_list.view_tasks()

        elif choice == 3:
            task = input("Enter task to update: ")
            new_status = input("Enter new status (pending/done): ")
            todo_list.update_task(task, new_status)

        elif choice == 4:
            task = input("Enter task to delete: ")
            todo_list.delete_task(task)

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()