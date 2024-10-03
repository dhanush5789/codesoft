import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")

        
        self.tasks = []

       
        self.title_label = tk.Label(root, text="To-Do List", font=("Arial", 18))
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(root, width=30, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        
        self.add_task_button = tk.Button(root, text="Add Task", width=15, font=("Arial", 12), command=self.add_task)
        self.add_task_button.pack(pady=10)

        self.task_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

       
        self.update_task_button = tk.Button(root, text="Update Task", width=15, font=("Arial", 12), command=self.update_task)
        self.update_task_button.pack(side=tk.LEFT, padx=10)

        self.delete_task_button = tk.Button(root, text="Delete Task", width=15, font=("Arial", 12), command=self.delete_task)
        self.delete_task_button.pack(side=tk.RIGHT, padx=10)

   
    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

 
    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task != "":
                self.tasks[selected_task_index[0]] = new_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a task.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
