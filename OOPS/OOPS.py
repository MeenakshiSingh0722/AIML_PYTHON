# car class with attribute brand and model then instance of class
# class Car:
#     def __init__(self, brand, model):
#         self.brand=brand
#         self.model=model
#
#     def fullName(self):
#         return f"{self.brand} {self.model}"
#
# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size=battery_size
#
# # myCar=Car("toyota","corolla")
# # print(myCar.brand, myCar.model)
# # print(myCar.fullName())
#
# my_tesla=ElectricCar("tesla","model S ","76kwh")
# print(my_tesla.model )
# print(my_tesla.fullName())

# ENCAPSULATION
# class Car:
#     def __init__(self, brand, model):
#         self.__brand=brand
#         self.model=model
#
#     def get_brand(self):
#         return self.__brand+ " !"
#
#     def full_name(self):
#         return f"{self.__brand} {self.model}"
#
# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size=battery_size
#
#
# my_tesla=ElectricCar("tesla","model S ","76kwh")
# print(my_tesla.get_brand())
# print(my_tesla.__brand)

# POLYMORPHISM
# class Car:
#     def __init__(self, brand, model):
#         self.__brand=brand
#         self.model=model
#
#     def get_brand(self):
#         return self.__brand+ " !"
#
#     def full_name(self):
#         return f"{self.__brand} {self.model}"
#
#     def fuel_type(self):
#         return "petrol or diesel"
#
# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size=battery_size
#
#     def fuel_type(self):
#         return "Electric charge"
#
# safari = Car("tata","safari")
# print(safari.fuel_type())

# CLASS variable: add class var. to car that keeps track of the num of cars created


# static method: add a static method to thr car class that returns a general description of a car
