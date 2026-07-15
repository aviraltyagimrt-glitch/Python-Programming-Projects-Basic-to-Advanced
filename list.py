L = ["Hello","Everyone",4,5,6,["let's","see",6,7,"!"],90,"End"]
print(L[5][0][2:4])
flat = []
for item in L:
    if isinstance(item, list):
        flat.extend(item)
    else:
        flat.append(item)
if 7 in flat:
    print("Yes, 7 is present in the list")
else :
    print("No, 7 is not present in the list")
for i in L:
    print(i,end = ", ")
lst = [i*i for i in range(10) if i%2 == 0]
print(lst)
(L.append("7"))
print(L)
(L.reverse())
print(L)
L2 = [212,4,8,1,2,3,4,7,3,4,1,2,28]
(L2.sort())
print(L2)
(L2.sort(reverse=True))
print(L2)
print(L2.index(1)) # Returns the index of the first occurence of that value  
print(L2.count(1)) 
m = L2.copy() # Copies one List into another 
m [2] = 27 
print(L2)
print(m)
L.insert(1,8)
print(L)
L[4].insert(2,27) # You cannot insert inside nested list using this method (index,value)
print(L)
z = [300,500,800]
L2.extend(z)
print(L2)
x = L2 + z
print(x)
print(len(L))