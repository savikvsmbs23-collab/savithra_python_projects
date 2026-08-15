from vehicle import Vehicle

class Boat(Vehicle):
    def __init__(self, brand, speed, boat_type):
        super().__init__(brand, speed)
        self.boat_type = boat_type
    def move(self):
        return f"Boat is sailing at {self.speed}km/h."
    def anchor(self):
        return "Anchor dropped!"
