number = 98
if number > 50:
    print("Yes")



number = 28
if number > 50:
    print("Yes")
else:
    print("Invalid Input")




number = 28
if number > 50:
    print("Yes")
elif number < 50:
    print("No")
else:
    print("Number out of range")



lst1 = ['red', 'yellow', 'blue', 'violet']
print("List 1 :", lst1)
print(type(lst1))

lst2 = [1, 'yellow', 'blue', 0.7, 'True']
print("List 2 :", lst2)
print(type(lst2))



number = int(input("Enter Number to Check"))
print("Number to be checked :", number)

if number>0:
  print("This is a positive number")

elif number<0:
  print("This is a negative number")

else:
  print("This is neutral")




  number = int(input("Enter Number to check"))
print("Number to be checked :", number)

if number%2==0 :
  print("This is an even number")

else:
  print("This is an odd number")






lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("Length of list:", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('Papaya')
print("Updated List :", lst)

lst.remove('Guava')
print("Updated List :", lst)

lst.sort()
print("Sorted List:", lst)

lst.pop(1)
print("Updated List :", lst)

lst.reverse()
print("Reversed List :", lst)

print("Multiplication on List :", lst*2)

lst = lst[:4]
print("Sliced List :", lst)

lst.clear()
print("Updated List :", lst)

