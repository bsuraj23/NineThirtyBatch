class sample():
    def __init__ (self,name,age):
        self.name=name
        self.age=age
        print("i am a constructor class")
    def display(self):
        return self.name,self.age
obj=sample("teju varma",21)
print(obj.display())   