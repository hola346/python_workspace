string = "hola que tal por aquí    "

print(string[0:4])

string2 = string[0:4]
print(string2)

string3 = string + " " + string2
print(string3)

string3.find(string2)

string2 in string3  # contains

# split in two:

string4 = string.split("t")
print(string4)

print(string4[1])

# trim -remove spaces

string5 = string.strip()  # seems like strip only removes final spaces
# you also have methods lstrip - rstrip - left, right
print(string)
print(string5)
print(string5.replace(" ", ""))  # this removes - replace all spaces
