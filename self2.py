class Adder:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

x = Adder(3, 4)
x.add()