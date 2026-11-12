    
class Panda:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        return x + y


p = Panda(10, 5)

print("Sum of 10 and 5 is:", p.add(p.x, p.y))