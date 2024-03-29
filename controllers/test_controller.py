from models.test_model import TestModel
from views.test_view import TestView

class TestController:
    def __init__(self, root):
        self.model = TestModel()
        self.view = TestView(root, self)

    def on_button_click(self):
        name = self.view.entry.get()
        self.model.set_name(name)
        greeting = self.model.get_greeting()
        self.view.update_label(greeting)

    def on_close(self):
        # ウィンドウが閉じられたときの処理
        self.view.root.destroy()