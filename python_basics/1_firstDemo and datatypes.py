print("Hello")

# comments here

# variables - you don't need to declare type:

a = 3
print(a)

str = "Hello world"
print(str)

a, b, c = 4, 4.6, "cocina"

print(c)
print("Value is", b)  # concatenate dif types, see 'print("{} {}".format("value is",b))'
print("{} {}".format("value is", b))
print(type(b))
print(type(a))

# contact 2 strings:
str1 = "Hello hello again"
str2 = "Bye, bye my love"
print(str1, "SPACE HERE", str2, "ALSO ADDING NUMBERS", a, b)

# LISTS
list1 = [1, 2, "apples", 7.908]
print(list1)
print(list1[3])
print(list1[-2])
print(list1[0:2])  # last index not included

print(list1.count)
list1.insert(
    4, "new element"
)  # add new elem to your list on index position, does not remove previous
print(list1)
list1.insert(0, "update element")
print(list1)
list1.insert(2, "another element")
print(list1)
list1.append("append element at the end")  # add new elem at the end, no index needed
print(list1)

list1[1] = "elem 1 changed"  # changing elem, not using a method, but direct assignation
print(list1)

del list1[0]  # remove elem from the list
print(list1)

# TUPLE - Same as LIST, but cannot be changed-modified

tup = (67.8, "jarl", 3)
print(type(tup))
print(type(list1))

# del tup[0]
print(tup)

# Dictionary: similar as JSON - key - value

dic = {"name": "David", "age": 32, "comment": "helloooo"}
print(dic)
print(type(dic))

print(dic["comment"])
