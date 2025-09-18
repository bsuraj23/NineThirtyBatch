class Name:
    def __init__(self, name: str):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"  
    
nandu=Name("Nandu")
print(nandu.greet())