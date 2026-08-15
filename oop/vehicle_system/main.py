from car import Car
from boat import Boat

car = Car("Toyota", 120, 4)
boat = Boat("Yamaha", 60, "speedboat")


print(car.move())
print(car.honk())
print(boat.move())
print(boat.anchor())
