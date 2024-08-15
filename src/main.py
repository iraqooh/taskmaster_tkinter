import tkinter as tk
from ui import TaskmasterUI

def main():
    root = tk.Tk()
    app = TaskmasterUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
