import tkinter as tk
import subprocess

# setup_env.shを実行して環境変数を設定
subprocess.call("setup_env.sh", shell=True)

from controllers.TestController import TestController

def main():
    root = tk.Tk()
    app = TestController(root)
    root.mainloop()

if __name__ == "__main__":
    main()