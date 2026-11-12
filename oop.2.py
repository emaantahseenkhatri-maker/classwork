class Rectangle():
    def __init__(self, l, w):
        self.width = w
        self.length = l

    def rectangle_area(self):
        return self.width * self.length

newRectangle = Rectangle(10, 20)
print("Dimension of Rectangle - Length : %d, Width : %d" % (newRectangle.length, newRectangle.width))
print("Area of Rectangle:", newRectangle.rectangle_area())