import tkinter as tk
from controllers.test_controller import TestController

def main():
    root = tk.Tk()
    app = TestController(root)
    root.mainloop()

if __name__ == "__main__":
    main()