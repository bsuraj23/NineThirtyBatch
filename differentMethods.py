# different methods of defining a class in python
class Person:
    #instance method
    def person_details(self,name,age):
        self.name=name
        self.age=age
        print("instance method")
        print("name:",self.name)
        print("age:",self.age)
    #class method
    @classmethod
    def person_info(cls,name,age):
        cls.name=name
        cls.age=age
        print("class method")
        print("name:",cls.name)
        print("age:",cls.age)       
    #static method
    @staticmethod
    def person_data(name,age):
        print("static method")
        print("name:",name)
        print("age:",age)
obj=Person()
obj.person_details("sri",20)    
obj.person_info("keerthana",25)
obj.person_data("sri keerthana",22)
print(Person.person_details)  
print(Person.person_info)  
print(Person.person_data)     