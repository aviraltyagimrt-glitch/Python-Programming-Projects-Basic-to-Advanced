 # This is an example of multiline string
x = """Hello everyone today we are learning how to write a multiline string using just triple quotes 
and without a "back slash n" for a 'new' line"""
print(x)
# This is an example of string inside an string
x2 = "So this is an example of how you can use double quote like this using \"Aviral Tyagi\" like this"
print(x2)

# # String Slicing and Iteration
for i in x:
    print(i,end = "")
print("\n")
str = "Aviral Tyagi"
print(len(str))
print(str[0:12])
print(str[:12:2])
print(str[::4])
print(str[:-1])
print(str[-8:-1:2])
print(str[-1:len(str)-10:-2])
print(len(x))
print(x[0:123:8])
print(len(x2))
print(x2[0:84])

# String Methods 
# Note :- Strings are immutable and hence whenever String Methods are used a new string is created instead of Changing the original one . 
a = "Aviral"
a2 = "AVIRAL"
g = "gaurika"
g2 = "!!Gaurika!!"
z1 = "Aviral Tyagi"
z2 = "HelloandWelcometoVSCodeon9"
z3 = "   "
print(a)
print(a.isupper()) # Checks whether each and every letter in the string is in upper .
print(g.islower()) # Checks whether each and every letter in the string is in lower .
print(g2.islower()) 
print(a2.isupper())
print(a.upper()) # Converts all the letter of the string into upper .
print(a2.lower()) # Converts all the letter of the string into lower .
print(g2.lower())
print(g.upper())
print(g2.rstrip("!")) # Removes extra trailing spaces from the right .
print(g2.lstrip("!")) # Removes extra trailing spaces from the left .
print(g2.strip("!"))  # Removes extra trailing spaces from both sides .
print(a.replace("Aviral","Aviral Tyagi")) # Replaces the first string with the second string .
print(g2.split("!")) # Splits from the character given and returns an List .
print(z1.split(" ")) # Splits from the character given and returns an List .
print(g.capitalize()) # Capitalize Capitalizes the first Letter of the string and rest all into lowercases if not done yet .
print(z1.center(51)) # Centres the string upto which the number is given .
print(g.count("a")) # Counts the number of time the specific string occours in your main string and checks exact Alphabet if lower so lower and if upper so upper only .
print(z1.count("a")) # Same Counts and returns answer in integer number .
print(g.endswith("a")) # Checks whether the given strings ends with the provided string and returns the answer in Boolean Form .
print(g2.endswith("!!")) # Checks whether the given strings ends with the provided string and returns the answer in Boolean Form .
print(g2.endswith("r",0,6)) # Checks whether the given strings ends with the provided string and returns the answer in Boolean Form .
print(z1.find("A")) # Checks the provided string and return the first occurence of that string and Returns -1 if not founded , need to Enter exact string if upper so upper or lower so lower . 
print(z1.index("T")) # Checks the provided string and return the first occurence of that string and Returns ValueError if not founded , need to Enter exact string if upper so upper or lower so lower .
print(z2.isalnum()) # Should consist A-Z a-z or 0-9 not even spaces or any special punctuations , characters . 
print(g.isalpha()) # Should only consist of Alphabets not even an single number , spaces or any punctuation or special characters .
print(z2.isprintable()) # Checks whether the given string is printable or not , usually \n , \t are non-printable . 
print(z3.isspace()) # Checks whether their are only spaces or not , even a single character,number any special punctuation or anything is not considered . 
print(z1.istitle()) # Checks whether the first letter of each word is in upper case or not and rest all in lower case or not .
print(g2.startswith("!!")) # Checks whether the given strings starts with the provided string and returns the answer in Boolean Form .
print(a.swapcase()) # Swaps the case of each letter in the string if upper so lower and if lower so upper .
print(a2.casefold()) # similar to lower() but more aggressive and strong.
print(a.encode()) # return a encoded version of a string.
print(a.format()) # format specific values inside the string.

