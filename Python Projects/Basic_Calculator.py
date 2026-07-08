#Let's Make a Simple Calculator in Python
print("Press 1 if you want to do calculations with only 2 integer numbers !!\n")
print("Press 2 if you want to do calculations with 1 integer number and 1 decimal number !!\n")
print("Press 3 if you want to do calculations with only 2 decimal numbers !!\n")
print("Press 4 if you want to exit the calculator !!\n")
a = int(input("Enter the number according to your choice :\n"))
if (a == 1):
    z1 = int(input("Enter the First Number\n"))
    z2 = int(input("Enter the Second Number"))
    print("Press 1 if you want to add these two numbers\n")
    print("Press 1 if you want to add these two numbers\n")
    print("Press 1 if you want to add these two numbers\n")
    print("Press 1 if you want to add these two numbers\n")
    print("Press 1 if you want to add these two numbers\n")
    z3 = int(input("Enter the number according to your choice\n"))
    if (z3 == 1):
        print(f"The sum of {z1} and {z2} is {z1+z2}")
    elif (z3 == 2):
        print(f"The subtraction of {z1} and {z2} is {z1-z2}")
    elif (z3 == 3):
        print(f"The multiplication of {z1} and {z2} is {z1*z2}")
    elif (z3 == 4):
        if z2 == 0:
            print("Cannot divide by zero")
        else:
        print(f"The division of {z1} and {z2} is {z1/z2}")
    elif (z3 == 5):
        if z2 == 0:
            print("Cannot divide by zero")
        else:
        print(f"The floor division of {z1} and {z2} is {z1//z2}")
    elif (z3 == 6):
        print(f"The modulus of {z1} and {z2} is {z1%z2}")
elif(a == 2):

elif(a == 3):

else:
    print("Enter the number from the choices mentioned above !!")