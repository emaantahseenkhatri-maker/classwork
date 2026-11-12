class food:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def yummy(self, good):
        return "{} are full {}".format(self.name, good)

    def hungry(self):
        return "{} are now hungry".format(self.name)

donuts = food("Donuts", 10)

print(donuts.yummy("'Happy'"))
print(donuts.hungry())

noodles = food("Noodles", 5)

print(noodles.yummy("'Yummy'"))
print(noodles.hungry())
