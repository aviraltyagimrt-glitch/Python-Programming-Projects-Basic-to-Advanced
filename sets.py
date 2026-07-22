a = set()
print(type(a))
b = {1,2,3,1,"Aviral","!","Hii",frozenset({1,2,2,1,"Hello"})}
print(b)
for i in b:
    print(i)
c = {1,2,4,5,7,"Tyagi"}
print(b.union(c))
c.update(b)
print(b)
print(c)
print(b.intersection(c))
b.intersection_update(c)
print(b)
b.symmetric_difference_update(c)
print(b)
b.difference(c)
print(b)
print(c.isdisjoint(b))
print(c.issuperset(b))
print(c.issubset(b))
c.add("Gaurika")
print(c)
c.remove(1)
print(c)
c.discard(3) # It will not raise an error if not Present rather than remove 
print(c)
print(c.pop())
#del c
#c.clear()
if "Gaurika" in c:
    print("Aviral is present")
else:
    print("Aviral is not present")
print(c)
found = False
for item in b:
    if isinstance(item, frozenset) and "Hello" in item:
        found = True
        break

print(found)  # True
nested = frozenset({1, 2, 1, "Hello"})
print("Hello" in nested)  # True