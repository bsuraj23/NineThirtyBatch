class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def calculate_bonus(self):
        bonus = self.salary 
        return 0
class Manager(Employee):
    def calculate_bonus(self):
        bonus = self.salary * 0.2
        return bonus   
class Developer(Employee):
    def calculate_bonus(self):
        bonus = self.salary * 0.1
        return bonus
emp1 = Manager("keerthana", 35, 80000)
emp2 = Developer("srili", 28, 60000)
print(f"{emp1.name}'s bonus: {emp1.calculate_bonus()}")
print(f"{emp2.name}'s bonus: {emp2.calculate_bonus()}")    
         