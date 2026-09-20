## Question 6: Class Hierarchy — Vehicle, Car, Bike##
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        print(f"{self.brand} is a vehicle that can travel at {self.speed} km/h.")


class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def describe(self):  # overriding the base class method
        print(f"{self.brand} is a car with {self.doors} doors, travelling at {self.speed} km/h.")


class Bike(Vehicle):
    def __init__(self, brand, speed, has_gears):
        super().__init__(brand, speed)
        self.has_gears = has_gears

    def describe(self):  # overriding the base class method
        gear_text = "with gears" if self.has_gears else "single-speed"
        print(f"{self.brand} is a {gear_text} bike, travelling at {self.speed} km/h.")


# Demonstration
vehicles = [
    Vehicle("Generic Transport", 60),
    Car("Toyota Corolla", 180, 4),
    Bike("Mountain Bike", 25, True),
]

for v in vehicles:
    v.describe()