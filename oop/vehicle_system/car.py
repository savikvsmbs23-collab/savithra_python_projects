from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(brand, speed)
        self.num_doors = num_doors
    def move(self):
        return f"Car is driving at {self.speed}km/h"
    def honk(self):
        return "Beep beep!"
