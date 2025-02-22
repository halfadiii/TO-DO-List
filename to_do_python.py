import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        with open(file_path, 'a') as file:
            file.write(task + '\n')
        task_entry.delete(0, tk.END)
        list_tasks()
    else:
        messagebox.showwarning("Warning", "The task cannot be empty.")

def list_tasks():
    listbox.delete(0, tk.END)
    try:
        with open(file_path, 'r') as file:
            for task in file:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        with open(file_path, 'r') as file:
            tasks = file.readlines()
        del tasks[task_index]
        with open(file_path, 'w') as file:
            file.writelines(tasks)
        list_tasks()
    except IndexError:
        messagebox.showerror("Error", "Please select a task to delete.")

root = tk.Tk()
root.title("ToDo List")

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=20)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=10)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=20)

delete_button = tk.Button(root, text="Delete Selected Task", command=delete_task)
delete_button.pack(pady=10)

#task listing
file_path = "todo.txt"
list_tasks()

#GUI
root.mainloop()
