class keerthana:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age >= 0:  # Basic validation
            self.__age = age
        else:
            print("Age cannot be negative")
obj=keerthana("sri",20)
print(obj.get_name())  # Accessing name using getter
print(obj.get_age())   # Accessing age using getter
obj.set_name("keerthana")  # Modifying name using setter
obj.set_age(25)
print(obj.get_age)            # Modifying age using setter
print(obj.get_name())  # Accessing name using getter
print(obj.get_age())   # Accessing age using getter