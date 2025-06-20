"""
    OOPS - 
    Basic Class and Objects
"""

"""
    Add a method to the car class that displays the full name of the car (brand and model)
"""

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name_of_car(self):
        return f"Full name of the car is: {self.brand} {self.model}"

object_of_class_car = Car("Honda","civic")
print(object_of_class_car.brand)
print(object_of_class_car.model)
print(object_of_class_car.full_name_of_car())