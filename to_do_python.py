import sys

def add_task(task, file_path):
    with open(file_path, 'a') as file:
        file.write(task + '\n')
    print("Task added.")

def list_tasks(file_path):
    try:
        with open(file_path, 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("ToDo List:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task.strip()}")
            else:
                print("No tasks to show.")
    except FileNotFoundError:
        print("No tasks to show.")

def delete_task(task_index, file_path):
    try:
        with open(file_path, 'r') as file:
            tasks = file.readlines()
        if tasks and 0 < task_index <= len(tasks):
            del tasks[task_index - 1]
            with open(file_path, 'w') as file:
                file.writelines(tasks)
            print("Task deleted.")
        else:
            print("Invalid task index.")
    except FileNotFoundError:
        print("No tasks to show.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add/list/delete] [task]")
    else:
        action = sys.argv[1]
        file_path = "todo.txt"
        
        if action == "add" and len(sys.argv) == 3:
            add_task(sys.argv[2], file_path)
        elif action == "list":
            list_tasks(file_path)
        elif action == "delete" and len(sys.argv) == 3:
            try:
                task_index = int(sys.argv[2])
                delete_task(task_index, file_path)
            except ValueError:
                print("Please enter a valid task index.")
        else:
            print("Invalid command or number of arguments.")
