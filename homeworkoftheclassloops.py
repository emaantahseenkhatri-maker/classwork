num =20
print("Table oftwenty")
for i in range(1, 11):
    print (f"20 x {i} = {num * i}")

num2=1
sum=0
while(num2<=20):
    sum=sum+num2
    num2= num2+1
print("Sum of numbers from 2 to 20 is:", sum)

num=29
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")



    num = 5
sum = 0
while(num<=50):
  sum = sum+num
  num = num+1

print("Sum of First 50 Natural Numbers :", sum)