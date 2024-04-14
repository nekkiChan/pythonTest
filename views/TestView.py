# view/test_view.py

import tkinter as tk

class TestView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Tkinter Test App")

        # ウィンドウの初期サイズを設定
        self.root.geometry("400x300")

        self.label = tk.Label(root, text="Enter your name:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Say Hello", command=self.controller.on_button_click)
        self.button.pack(pady=10)

        # ウィンドウが閉じられたときの処理を設定
        self.root.protocol("WM_DELETE_WINDOW", self.controller.on_close)

    def update_label(self, text):
        self.label.config(text=text)
