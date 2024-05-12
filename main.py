import tkinter as tk
from dotenv import load_dotenv

# .envファイルの内容を読み込見込む
load_dotenv()

from controllers.TestController import TestController

def main():
    root = tk.Tk()
    app = TestController(root)
    root.mainloop()

if __name__ == "__main__":
    main()