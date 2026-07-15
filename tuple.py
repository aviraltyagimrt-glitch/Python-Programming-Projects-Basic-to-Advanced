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
T3 = (1,2,3,4,5,1,2,1,7,8,27)
print(T3.count(1))
print(T2+T3)
T4 = list(T3)
T4.append(2009)
print(T4)
T4.pop(3)
print(T4)
T4[0] = "Hii"
print(T4)
T5 = tuple(T4)
print(T5)
print(T3.index(1))
z = T3.index(1,2,9) # (value,start,stop)
print(z)
print(len(T))