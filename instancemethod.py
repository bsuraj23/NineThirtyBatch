#instance method
class Person:
    @staticmethod
    def person_details(name,age):
        print(name)
        print(age)
    def add():
        return 10+20
        print("instance method")
print(Person.person_details("kee", 25))
print(Person.add())
