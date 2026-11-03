num =17
print("Table of Seventeen")
for i in range(1, 11):
    print (f"17 x {i} = {num * i}")

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