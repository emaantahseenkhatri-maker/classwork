class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

newCircle = Circle(5)
print("Radius of Circle :", newCircle.radius)
print("Area of Circle :", newCircle.area())


newCircle2 = Circle(12)
print("Radius of Circle :", newCircle2.radius)
print("Area of Circle :", newCircle2.area())
