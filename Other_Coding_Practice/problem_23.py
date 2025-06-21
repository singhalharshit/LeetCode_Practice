"""
    OOPS - 
    Basic Class and Objects
"""

"""
    Add a method to the car class that displays the full name of the car (brand and model)
"""

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name_of_car(self):
        return f"Full name of the car is: {self.__brand} {self.model}"

object_of_class_car = Car("Honda","civic")
print(object_of_class_car.__brand)
print(object_of_class_car.model)
print(object_of_class_car.full_name_of_car())

"""
    Create an Electric Car class that inherits from the Car class and has an additional attribute battery_size
"""

class ElectricCar(Car):
    def __init__(self, brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    

ElectricCar_Obj = ElectricCar("Tesla","Model S","85kWh")
print(ElectricCar_Obj.model)
print(ElectricCar_Obj.full_name_of_car())

"""
    Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it
"""

# print(ElectricCar_Obj.get_brand())