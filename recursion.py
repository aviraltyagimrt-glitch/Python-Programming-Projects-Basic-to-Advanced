def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n-1)
a = int(input("Enter the number whose factorial you want to print\n"))
z = factorial(a)
print(f"The factorial of {a} is {z}")

def fibonacci(x):
    if (x == 0):
        return 0
    elif (x == 1):
        return 1
    else:
        return fibonacci(x-1) + fibonacci (x-2)
b = int(input("Enter the number whose Fibonacci series you want to print\n"))
for i in range (b):
    print(fibonacci(i),end=" ")
print()
# OTHER WAYS TO PRINT THE SAME OUTPUT
series = []      
for i in range(b):
    series.append(fibonacci(i))
print(series)
series = [fibonacci(i) for i in range(b)]
print(series)
c = fibonacci(b)
print(f"The fibonacci series of {b} is {c}")