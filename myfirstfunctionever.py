def greet(name):
   print("Hello, " + name + ". Good to see you!")
greet("penguin")


def absolute_value(num):
   if num >= 0:
       return num
   else:
       return -num
print("absolute_value of 89:", absolute_value(89))
print("absolute_value of -189:", absolute_value(-189))


def ispalindrone(string):
  left_pos = 0
  right_pos = len(string) - 1
  while left_pos < right_pos:
      if string[left_pos] != string[right_pos]:
          return False
      left_pos += 1
      right_pos -= 1
  return True

print("is 'racecar' a palindrone?", ispalindrone("racecar"))
print("is 'hello' a palindrone?", ispalindrone("hello"))

