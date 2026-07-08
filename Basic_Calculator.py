#Let's Make a Simple Calculator in Python
while True:
    print("\nPress 1 if you want to do calculations with only 2 integer numbers !!")
    print("Press 2 if you want to do calculations with 1 integer number and 1 decimal number !!")
    print("Press 3 if you want to do calculations with only 2 decimal numbers !!")
    print("Press 4 if you want to exit the calculator !!")
    a = int(input("Enter the number according to your choice :\n"))
    if (a == 1):
        z1 = int(input("Enter the First Number\n"))
        z2 = int(input("Enter the Second Number\n"))
        print("Press 1 if you want to add these two numbers")
        print("Press 2 if you want to subtract these two numbers")
        print("Press 3 if you want to multiply these two numbers")
        print("Press 4 if you want to divide these two numbers")
        print("Press 5 if you want to do floor division with these two numbers")
        print("Press 6 if you want to do calculate modulus of these two numbers")
        z3 = int(input("Enter the number according to your choice\n"))
        if (z3 == 1):
            print(f"The sum of {z1} and {z2} is {z1+z2}")
        elif (z3 == 2):
            print(f"The subtraction of {z1} and {z2} is {z1-z2}")
        elif (z3 == 3):
            print(f"The multiplication of {z1} and {z2} is {z1*z2}")
        elif (z3 == 4):
            if (z2 == 0):
                print("Cannot divide by zero")
            else:
                print(f"The division of {z1} and {z2} is {z1/z2}")
        elif (z3 == 5):
            if (z2 == 0):
                print("Cannot divide by zero")
            else:
                print(f"The floor division of {z1} and {z2} is {z1//z2}")
        elif (z3 == 6):
            print(f"The modulus of {z1} and {z2} is {z1%z2}")
        else:
            print("Enter the number form the options mentioned above")
    elif(a == 2):
        print("Press 1 if you want your first number to be an integer and the 2nd one to be an float")
        print("Press 2 if you want your first number to be an float value and the 2nd one to be an integer")
        k = int(input("Enter the number according to your choice\n"))
        if (k == 1):
            z1 = int(input("Enter the First Number\n"))
            z2 = float(input("Enter the Second Number\n"))
            print("Press 1 if you want to add these two numbers")
            print("Press 2 if you want to subtract these two numbers")
            print("Press 3 if you want to multiply these two numbers")
            print("Press 4 if you want to divide these two numbers")
            print("Press 5 if you want to do floor division with these two numbers")
            print("Press 6 if you want to do calculate modulus of these two numbers")
            z3 = int(input("Enter the number according to your choice\n"))
            if (z3 == 1):
                print(f"The sum of {z1} and {z2} is {z1+z2}")
            elif (z3 == 2):
                 print(f"The subtraction of {z1} and {z2} is {z1-z2}")
            elif (z3 == 3):
                print(f"The multiplication of {z1} and {z2} is {z1*z2}")
            elif (z3 == 4):
                if (z2 == 0):
                    print("Cannot divide by zero")
                else:
                    print(f"The division of {z1} and {z2} is {z1/z2}")
            elif (z3 == 5):
                if (z2 == 0):
                    print("Cannot divide by zero")
                else:
                    print(f"The floor division of {z1} and {z2} is {z1//z2}")
            elif (z3 == 6):
                print(f"The modulus of {z1} and {z2} is {z1%z2}")
            else :
                print("Enter number from the options mentioned above")
        elif (k == 2):
            z1 = float(input("Enter the First Number\n"))
            z2 = int(input("Enter the Second Number\n"))
            print("Press 1 if you want to add these two numbers")
            print("Press 2 if you want to subtract these two numbers")
            print("Press 3 if you want to multiply these two numbers")
            print("Press 4 if you want to divide these two numbers")
            print("Press 5 if you want to do floor division with these two numbers")
            print("Press 6 if you want to do calculate modulus of these two numbers")
            z3 = int(input("Enter the number according to your choice\n"))
            if (z3 == 1):
                print(f"The sum of {z1} and {z2} is {z1+z2}")
            elif (z3 == 2):
                print(f"The subtraction of {z1} and {z2} is {z1-z2}")
            elif (z3 == 3):
                print(f"The multiplication of {z1} and {z2} is {z1*z2}")
            elif (z3 == 4):
                if (z2 == 0):
                    print("Cannot divide by zero")
                else:
                    print(f"The division of {z1} and {z2} is {z1/z2}")
            elif (z3 == 5):
                if (z2 == 0):
                    print("Cannot divide by zero")
                else:
                    print(f"The floor division of {z1} and {z2} is {z1//z2}")
            elif (z3 == 6):
                print(f"The modulus of {z1} and {z2} is {z1%z2}")
            else :
                print("Enter the number from the options mentioned above")

    elif (a == 3):
        z1 = float(input("Enter the First Number\n"))
        z2 = float(input("Enter the Second Number\n"))
        print("Press 1 if you want to add these two numbers")
        print("Press 2 if you want to subtract these two numbers")
        print("Press 3 if you want to multiply these two numbers")
        print("Press 4 if you want to divide these two numbers")
        print("Press 5 if you want to do floor division with these two numbers")
        print("Press 6 if you want to do calculate modulus of these two numbers")
        z3 = int(input("Enter the number according to your choice\n"))
        if (z3 == 1):
            print(f"The sum of {z1} and {z2} is {z1+z2}")
        elif (z3 == 2):
            print(f"The subtraction of {z1} and {z2} is {z1-z2}")
        elif (z3 == 3):
            print(f"The multiplication of {z1} and {z2} is {z1*z2}")
        elif (z3 == 4):
            if (z2 == 0):
                print("Cannot divide by zero")
            else:
                print(f"The division of {z1} and {z2} is {z1/z2}")
        elif (z3 == 5):
            if (z2 == 0):
                print("Cannot divide by zero")
            else:
                print(f"The floor division of {z1} and {z2} is {z1//z2}")
        elif (z3 == 6):
            print(f"The modulus of {z1} and {z2} is {z1%z2}")
        else:
            print("Enter the number from the options mentioned above")

    elif (a == 4):
        print("Thank you for using the calculator")
        print("Developed by Aviral Tyagi")
        break
    else:
        print("Enter the number from the choices mentioned above !!")