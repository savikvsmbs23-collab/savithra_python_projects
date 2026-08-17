class Circle:
    pi = 3.14159

    def __init__(self, r):
        self.r =r
    def area(self):
        return f"The area is {self.pi * (self.r ** 2)}"
    def circumference(self):
        return f"The circumference is {2 * self.pi * self.r}"
    @classmethod
    def get_pi(cls):
        return f"Pi value is {cls.pi}"
    @staticmethod
    def is_valid_radius(radius):
        return radius > 0
