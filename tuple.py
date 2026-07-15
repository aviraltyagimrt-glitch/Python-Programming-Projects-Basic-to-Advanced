T = (8,27,"2009","Hello",("Everyone",78,667),"Oyee hoyee")
print(type(T))
print(T)
print(T[4][2])
if "2009" in T:
    print("Yes it's Present")
else:
    print("It's not present")
print(T[0:5])
print(T[-1])
T2 = T[:4]
print(T2)
for item in T[4]:
    if isinstance(item, int):
        print(item, "is a number")
    else:
        print(item, "is not a number")
for item in T[4]:
    try:
        int(item)
        print(item, "is a number")
    except ValueError:
        print(item, "is not a number")