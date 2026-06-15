"""Build a Car class with:

Attributes: brand, model, speed (starts at 0)
Methods:

accelerate() → increases speed by 10
brake() → decreases speed by 10
get_speed() → returns current speed



Then create 2 car objects and test all methods. 💪"""
class Car:
    def __init__(self,brand, model):

            self.brand = brand
            self.model = model
            self.speed = 0


    def accelerate(self):
        self.speed+=10
    def brake(self):
        if self.speed >0:
            self.speed-=10
    def get_speed(self):
        return f"The car {self.brand}'s speed is {self.speed}"

car1 = Car("toyota", "11A")
car2 = Car("audi","12A")
car1.accelerate()
car2.accelerate()
print(car1.get_speed())
car2 .brake()
print(car2.get_speed())
