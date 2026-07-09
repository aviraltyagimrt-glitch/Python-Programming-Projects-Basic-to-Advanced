# Basic if elif and else statements usage 
a = int(input("Enter your age :\n"))
if ( a >= 18 ):
    print(f"Congratulations your age is {a} and")
    print("Have you applied for DL (Y/N)")
    a = input("Enter your Response :\n")
    if (a =="Y" or a == "y"):
        print("You are eligible to drive")
    elif (a == "N" or a == "n"):
        print("You are eligible but you need to apply for the DL")
    else :
        print("Please select an option mentioned above")
elif (a < 18):
    print(f"Sorry your age is {a} and you are not eligible to drive")
else :
    print("Please select the option mentioned above\n")
