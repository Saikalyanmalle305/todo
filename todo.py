import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Input", "Please enter a task.")

def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to delete.")

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x430")
root.configure(bg="pink")

task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10, padx=10, fill=tk.BOTH)
add_button = tk.Button(root, text="Add Task", font=("Arial", 14), command=add_task)
add_button.pack(pady=5)

tasks_listbox = tk.Listbox(root, font=("Arial", 14), selectbackground="light pink", selectforeground="black")
tasks_listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Buttons to delete and clear tasks
delete_button = tk.Button(root, text="Delete Task", font=("Arial", 14), command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10, pady=5)
clear_button = tk.Button(root, text="Clear All", font=("Arial", 14), command=clear_tasks)
clear_button.pack(side=tk.RIGHT, padx=10, pady=5)


root.mainloop()
