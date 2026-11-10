class Penguin:    
 def __init__(self, name, age):
         self.name = name
         self.age = age

 def sing(self, song):
             return "{} sings {}".format(self.name, song)

 def dance(self):
             return "{} is now dancing".format(self.name)

dinkle = Penguin("dinkle", 10)
Berry = Penguin("Berry", 15)

print(dinkle.sing("Happy Birthday"))
print(Berry.dance())