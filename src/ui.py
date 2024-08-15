import tkinter as tk
from tkinter import messagebox
from task import Task
from storage import Storage
from export_import import ExportImport

class TaskmasterUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Taskmaster")
        self.master.geometry("800x600")

        # Create the main UI components
        self.create_menu()
        self.create_sidebar()
        self.create_main_section()

        # Load initial tasks
        self.load_tasks()

    def create_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        task_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Task", menu=task_menu)
        task_menu.add_command(label="New Task", command=self.new_task)
        task_menu.add_command(label="Export Tasks", command=self.export_tasks)
        task_menu.add_command(label="Import Tasks", command=self.import_tasks)
        task_menu.add_separator()
        task_menu.add_command(label="Settings", command=self.settings)
        task_menu.add_separator()
        task_menu.add_command(label="Exit", command=self.master.quit)

    def create_sidebar(self):
        sidebar = tk.Frame(self.master, width=200, bg='#f4f4f4')
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        tk.Button(sidebar, text="All Tasks", command=self.show_all_tasks).pack(fill=tk.X)
        tk.Button(sidebar, text="Upcoming Tasks", command=self.show_upcoming_tasks).pack(fill=tk.X)
        tk.Button(sidebar, text="Completed Tasks", command=self.show_completed_tasks).pack(fill=tk.X)
        tk.Button(sidebar, text="Categories", command=self.show_categories).pack(fill=tk.X)

    def create_main_section(self):
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.search_bar = tk.Entry(self.main_frame)
        self.search_bar.pack(fill=tk.X)

        self.task_list = tk.Listbox(self.main_frame)
        self.task_list.pack(fill=tk.BOTH, expand=True)

    def load_tasks(self):
        self.task_list.delete(0, tk.END)
        tasks = Storage.load_tasks()
        for task in tasks:
            self.add_task_to_listbox(task)

    def add_task_to_listbox(self, task):
        task_str = f"{task.name} - Due: {task.due_date} - Category: {task.category}"
        self.task_list.insert(tk.END, task_str)

    def new_task(self):
        def save_task():
            name = name_entry.get()
            due_date = due_date_entry.get()
            category = category_entry.get()
            priority = priority_var.get()
            task = Task(name, due_date, priority, category)
            Storage.add_task(task)
            self.add_task_to_listbox(task)
            new_task_window.destroy()

        new_task_window = tk.Toplevel(self.master)
        new_task_window.title("New Task")

        tk.Label(new_task_window, text="Name").grid(row=0, column=0)
        name_entry = tk.Entry(new_task_window)
        name_entry.grid(row=0, column=1)

        tk.Label(new_task_window, text="Due Date").grid(row=1, column=0)
        due_date_entry = tk.Entry(new_task_window)
        due_date_entry.grid(row=1, column=1)

        tk.Label(new_task_window, text="Category").grid(row=2, column=0)
        category_entry = tk.Entry(new_task_window)
        category_entry.grid(row=2, column=1)

        tk.Label(new_task_window, text="Priority").grid(row=3, column=0)
        priority_var = tk.StringVar(value="normal")
        tk.Radiobutton(new_task_window, text="High", variable=priority_var, value="high").grid(row=3, column=1)
        tk.Radiobutton(new_task_window, text="Normal", variable=priority_var, value="normal").grid(row=3, column=2)
        tk.Radiobutton(new_task_window, text="Low", variable=priority_var, value="low").grid(row=3, column=3)

        tk.Button(new_task_window, text="Save Task", command=save_task).grid(row=4, column=0, columnspan=4)

    def export_tasks(self):
        ExportImport.export_tasks()

    def import_tasks(self):
        ExportImport.import_tasks()
        self.load_tasks()

    def settings(self):
        messagebox.showinfo("Settings", "Settings dialog is not implemented yet.")

    def show_all_tasks(self):
        self.load_tasks()

    def show_upcoming_tasks(self):
        self.task_list.delete(0, tk.END)
        tasks = Storage.load_tasks()
        for task in tasks:
            if not task.completed and task.is_upcoming():
                self.add_task_to_listbox(task)

    def show_completed_tasks(self):
        self.task_list.delete(0, tk.END)
        tasks = Storage.load_tasks()
        for task in tasks:
            if task.completed:
                self.add_task_to_listbox(task)

    def show_categories(self):
        self.task_list.delete(0, tk.END)
        tasks = Storage.load_tasks()
        categories = set(task.category for task in tasks)
        for category in categories:
            self.task_list.insert(tk.END, f"--- {category} ---")
            for task in tasks:
                if task.category == category:
                    self.add_task_to_listbox(task)

    def search_tasks(self):
        query = self.search_bar.get().lower()
        self.task_list.delete(0, tk.END)
        tasks = Storage.load_tasks()
        for task in tasks:
            if query in task.name.lower() or query in task.category.lower():
                self.add_task_to_listbox(task)
