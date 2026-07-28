# Welcome to the game of coding and decoding
#Coding
import random
alphabets1 = "abcdefghijklmnopqrstuvwxyz"
alphabets2 = "abcdefghijklmnopqrstuvwxyz"
alphabets3 = "abcdefghijklmnopqrstuvwxyz"
alphabets4 = "abcdefghijklmnopqrstuvwxyz"
alphabets5 = "abcdefghijklmnopqrstuvwxyz"
alphabets6 = "abcdefghijklmnopqrstuvwxyz"
a1 = random.choice(alphabets1)
a2 = random.choice(alphabets2)
a3 = random.choice(alphabets3)
a4 = random.choice(alphabets4)
a5 = random.choice(alphabets5)
a6 = random.choice(alphabets6)
string = input("Enter your message\n")
if (len(string) > 2):
    l = list(string)
    n = l.pop(0)
    z = l.append(n)
    x1 = l.append(a1)
    x2 = l.append(a2)
    x3 = l.append(a3)
    x4 = l.insert(0,a4)
    x5 = l.insert(1,a5)
    x6 = l.insert(2,a6)
    str1 = "".join(l)
    print(str1)

else:
    reversed_string = string[::-1]
    print(reversed_string)

# Decoding
if (len(string) > 2):
    decoded_list = list(str1)
    removed_elements = decoded_list[3:-3]
    #print(removed_elements)
    popped_item = removed_elements.pop()
    #print(popped_item)
    #print(removed_elements)
    inserted_item = removed_elements.insert(0,popped_item)
    #print(removed_elements)
    new_string = "".join(removed_elements)
    print(new_string)

# elif (len(string) <=2 ):
#     decoded_list2 = list(string)
#     reversed_list = decoded_list2[::-1]
#     print("".join(reversed_list))

# else:
#     print("Enter Valid String format")

