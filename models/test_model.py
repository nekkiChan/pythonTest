class TestModel:
    def __init__(self):
        self.name = ""

    def set_name(self, name):
        self.name = name

    def get_greeting(self):
        return f"Hello, {self.name}" if self.name else "Hello!"