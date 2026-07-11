print("Press 1 to Print Good Morning")
print("Press 2 to Print Good Afternoon")
print("Press 3 to Print Good Evening")
print("Press 4 to Print Good Night")
a = int(input("Enter the number according to your choice:\n"))
match (a):
    case 1:
        print("Good Morning")
    case 2:
        print("Good Afternoon")
    case 3:
        print("Good Evening")
    case 4:
        print("Good Night")
    case _:
        print("Please enter the number from the options mentioned above")

