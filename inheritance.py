# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class inherits from Animal
class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Another child class
class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Create objects
a = Animal()
d = Dog()
c = Cat()

# Call the speak method
a.speak()  # Output: Animal makes a sound
d.speak()  # Output: Dog barks
c.speak()  # Output: Cat meows