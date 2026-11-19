def no_notes(a):
   Q = [2000, 500, 200, 100, 50, 20, 10,]
   x = 0
   for i in range (7):
      q = Q[i]
      x = a // q
      a = a - x * q
      print("Notes of {} ={} ", q, "is", x)

amount = int(input("Enter total amount: "))
no_notes(amount)