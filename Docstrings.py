def multiply():
    '''This Function will take two numbers and then will multiply them'''
    a = float(input("Enter your First Number:\n"))
    b = float(input("Enter your Second Number:\n"))
    c = a*b
    print(f"The multplication of {a:.2f} and {round(b,2)} is {c:.2f}")
multiply()
print(multiply.__doc__)