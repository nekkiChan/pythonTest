from models.TestModel import TestModel
from models.UsersModel import UsersModel
from views.TestView import TestView

class TestController:
    def __init__(self, root):
        self.model = TestModel()
        # self.usersModel = UsersModel()
        self.view = TestView(root, self)

    def on_button_click(self):
        name = self.view.entry.get()
        self.model.set_name(name)
        greeting = self.model.get_greeting()
        self.view.update_label(greeting)
        # self.usersModel.connect()
        # self.usersModel.create_table()
        # self.usersModel.disconnect()

    def on_close(self):
        # ウィンドウが閉じられたときの処理
        self.view.root.destroy()