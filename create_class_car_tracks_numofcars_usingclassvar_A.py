class car:
    count=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        car.count=car.count+1
    def __str__(self):
        return f"{self.brand}:{self.model}"
    @classmethod
    def number_of_cars(cls):
        return cls.count
print("Cars so far:", car.number_of_cars())

car1 = car("BMW", "M5")
print("Count of cars:", car.number_of_cars())
car2 = car("KIA", "CARNIVAL")
car3 = car("RANGEROVER", "VELAR")
car4 = car("AUDI","R8")
print("Count of cars:", car.number_of_cars())
print(car1, car2, car3, car4)