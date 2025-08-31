class Box:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

b = Box("Hello")
b.print_value()