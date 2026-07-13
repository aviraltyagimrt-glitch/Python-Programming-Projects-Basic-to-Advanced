def isgreater(a,b):
    if (a>b):
        print(f"{a} is greater than {b}")
    else :
        print(f"{b} is greater than {a}")
a = 78
b = 90
isgreater(a,b)

def issmaller(a,b):
    if (a<b):
        print(f"{a} is smaller than {b}")
    else :
        print(f"{b} is lesser than {a}")
c = 76
d = 75
issmaller(c,d)

def Hello(a,b,c,d):
    print(a+b*c/d)

Hello(25,2,3,4)

def Will_Create_it_Soon(a,b,c):
    pass # The pass function Keep the functions as it is and you can make changes whenever you want 

def names(Fname , Mname = "Weds" , Lname = "Gaurika" ):
    print("A very special Invitation" , Fname , Mname , Lname)
names("AVIRAL",Lname = "GAURIKA")

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return(f"The average is {(sum/len(numbers))}")

z = average(2,3,4,5,6)
print(z)

def copy(**names):
    print("Hello" , names["Fname"] , names["Mname"] , names["Lname"])
copy(Fname = "Gaurika" , Mname = "Weds" , Lname = "Aviral")