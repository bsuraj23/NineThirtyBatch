#class method
class Person:
    @classmethod
    def person_info(cls,name,age):
        cls.name=name
        cls.age=age
        print("class method")
        print("name:",cls.name)
        print("age:",cls.age)
print(Person.person_info("sri",20))        
