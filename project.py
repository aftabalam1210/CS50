# project.py

tasks = []

def main():
    while True:
        print("\nTask Tracker")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View All Tasks")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            mark_task_complete()
        elif choice == '3':
            view_all_tasks()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_task():
    task_name = input("Enter the task name: ")
    tasks.append({"name": task_name, "completed": False})
    print("Task added successfully!")

def mark_task_complete():
    view_all_tasks()
    task_index = int(input("Enter the index of the task to mark as complete: "))
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index.")

def view_all_tasks():
    print("\nAll Tasks:")
    for i, task in enumerate(tasks):
        status = "Complete" if task["completed"] else "Incomplete"
        print(f"{i}. {task['name']} - {status}")

def delete_task():
    view_all_tasks()
    task_index = int(input("Enter the index of the task to delete: "))
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

if __name__ == "__main__":
    main()
