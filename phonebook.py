import sys

def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts: ")), 5
    phonebook = []
    print(phonebook)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" % (i + 1))
        print("Note: * indicates mandatory fields")
        print(".............................................................................")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name*: ")))
            elif j == 1:
                temp.append(str(input("Enter number*: ")))
            elif j == 2:
                temp.append(str(input("Enter email address: ")))
            elif j == 3:
                temp.append(str(input("Enter date of birth (dd/mm/yyyy): ")))
            elif j == 4:
                temp.append
                (str(input("Enter category (Family/Friends/Work/Others): ")))
        phonebook.append(temp)
    print(phonebook)
    return phonebook

def menu():
    print("********************************************************************")
    print("\t\t\tPHONEBOOK DIRECTORY" , flush=False)
    print("********************************************************************")
    print("\tYou can now perform the following operations on this phonebook:")
    print("********************************************************************")
    print("1. Add a new contact")
    print("2. Delete a contact")
    print("3. Search for a contact")
    print("4. Display all contacts")
    print("5. Exit phonebook")
    print("********************************************************************")
    choice = int(input("Please enter your choice: "))
    return choice

def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name*: ")))
        elif i == 1:
            dip.append(str(input("Enter number*: ")))
        elif i == 2:
            dip.append(str(input("Enter email address: ")))
        elif i == 3:
            dip.append(str(input("Enter date of birth (dd/mm/yyyy): ")))
        elif i == 4:
            dip.append(str(input("Enter category (Family/Friends/Work/Others): ")))
    pb.append(dip)
    return pb

def remove_existing(pb):
    query = str(
        input("Please enter the name of the contact you wish to remove: "))
    temp = 0
    for i in range(len(pb)): 
        if query == pb[i][0]:
            temp +=1
            print("pb.pop(i)")
            print("Contact %s has been removed from the phonebook" % (query))
            return pb
    if temp == 0:
        print("Contact not found.")
        return pb 
def delete_all (pb):
    return pb.clear()

def search_existing(pb):
    query = str(
        input("Please enter the name of the contact you wish to search for: "))
    temp = 0
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp +=1
            print("Contact found: ", pb[i])
            return pb
    if temp == 0:
        print("Contact not found.")
        return pb