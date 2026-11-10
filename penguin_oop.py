class Penguin:
    species = "bird"

    def __init__(self, name, age):
     self.name = name
     self.age = age

dinkle= Penguin("Blu", 10)
Berry = Penguin("Woo", 15)


print("dinkle is a {}" .format(dinkle.species))
print("Berry is also a {}" .format(Berry.species))

print (" {} is {} years old" .format(Berry.name, Berry.age))
print (" {} is {} years old" .format(dinkle.name, dinkle.age))


