# To Do List application

tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        removed_task = tasks.pop(task_num-1)
        print(f"Task '{removed_task}' removed successfully!")
    except(IndexError, ValueError):
        print("Invalid Task number")



def show_tasks():
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nHere's your To-Do list:")
        for i,task in enumerate(tasks):
            print(i, task)




def main():
    while True:
        print("Options: 1. Add Task 2. Remove Task 3. Show Tasks 4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            show_tasks()
        elif choice == '4':
            print("Existing To-Do List")
            break
        else:
            print("Invalid choice, try again")

main()