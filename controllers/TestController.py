from models.TestModel import TestModel
from models.ConditionsModel import ConditionsModel
from views.TestView import TestView

class TestController:
    def __init__(self, root):
        self.model = TestModel()
        self.conditionsModel = ConditionsModel()
        self.view = TestView(root, self)

    def on_button_click(self):
        name = self.view.entry.get()
        self.model.set_name(name)
        greeting = self.model.get_greeting()
        self.view.update_label(greeting)
        self.conditionsModel.connect()
        self.conditionsModel.create_table()
        self.conditionsModel.disconnect()

    def on_close(self):
        # ウィンドウが閉じられたときの処理
        self.view.root.destroy()