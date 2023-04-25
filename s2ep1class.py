class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
        
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
    
    def get_mileage(self):
        return self.mileage
    
    def set_mileage(self, new_mileage):
        self.mileage = new_mileage
        
    def drive(self, miles):
        self.mileage += miles
        
my_car = Car("Toyota", "Camry", 2018)
print(my_car.get_make())   # Output: Toyota
print(my_car.get_model())  # Output: Camry
print(my_car.get_year())   # Output: 2018
print(my_car.get_mileage()) # Output: 0

my_car.drive(100)
print(my_car.get_mileage()) # Output: 100

my_car.set_mileage(5000)
print(my_car.get_mileage()) # Output: 5000


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self): 
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):  
        return (("*" * self.width) + "\n") * self.height if self.width <= 50 and self.height <= 50 else "Too big for picture."
    
    
shape = Rectangle(10, 5)
print(shape.get_area()) # Output: 50
print(shape.get_perimeter()) # Output: 30
print(shape.get_diagonal()) # Output: 11.180339887498949
print(shape.get_picture()) # Output: **********
