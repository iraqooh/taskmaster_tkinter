# Taskmaster

Taskmaster is a desktop to-do list application built using Python and Tkinter. It helps you efficiently manage your tasks by allowing you to create, prioritize, categorize, and set due dates for tasks. You can also import and export tasks from files and receive reminders for upcoming tasks.

## Features

- Task Management: Create, view, update, and delete tasks.
- Task Prioritization: Assign priority levels to tasks (High, Medium, Low).
- Task Categorization: Organize tasks into categories for better management.
- Due Dates: Set due dates and times to keep track of important deadlines.
- Task Completion: Mark tasks as completed using a checkbox.
- Notifications: Receive visual notifications for tasks that are due soon.
- Search Functionality: Search for tasks by name, due date, or category.
- Task Import/Export: Import and export tasks to/from JSON or CSV files.
- Settings: Customize the application settings to fit your preferences.

## Setup and Installation

### Prerequisites
- Python 3.x: Ensure Python is installed on your system.
- Tkinter: This is typically included with Python, but if it's not, you can install it via your package manager.
- Virtual Environment: It is recommended to use a virtual environment to manage dependencies.

### Installation

- Clone the Repository
```
git clone https://github.com/iraqooh/taskmaster_tkinter.git
cd taskmaster_tkinter
```

- Create a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

- Install Dependencies
```
pip install -r requirements.txt
```

Run the Application
```
python src/main.py
```

## Usage

### Task Management

- Create a New Task: Go to the "Task" menu and select "New Task". Fill in the task details and save.
- View Tasks: The main section displays all tasks by default. Use the sidebar to filter tasks (e.g., Upcoming, Completed, Categories).
- Update/Delete Tasks: Click the 3-dot icon next to a task to edit or delete it.
- Mark Task as Completed: Check the checkbox next to a task to mark it as completed.

### Import/Export Tasks

- Export Tasks: Go to the "Task" menu and select "Export Tasks". Choose JSON or CSV format.
- Import Tasks: Go to the "Task" menu and select "Import Tasks". Choose a JSON or CSV file to import.

### Notifications

A notification banner will appear between the search bar and task list for tasks that have just ended.

### Settings

Customize application settings via the "Settings" option in the "Task" menu.

## Running Tests

To run unit tests, ensure that you are in the virtual environment and execute:
```
python -m unittest discover tests
```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License—see the LICENSE file for details.
