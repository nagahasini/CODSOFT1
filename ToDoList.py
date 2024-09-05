class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"Task '{task}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\nTo-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task['completed'] else "Pending"
                print(f"{idx}. {task['task']} - {status}")

    def update_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            new_task = input("Enter the updated task: ")
            self.tasks[task_number - 1]['task'] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task number.")

    def mark_task_complete(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted successfully.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the new task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            try:
                task_number = int(input("Enter task number to update: "))
                todo_list.update_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                task_number = int(input("Enter task number to mark as complete: "))
                todo_list.mark_task_complete(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            try:
                task_number = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
