class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

p = Person("Hameed")
p.show()