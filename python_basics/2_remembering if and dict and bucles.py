age = int(input("How old are you? "))

if age < 18:
    print("your are little")
elif age > 18 and age < 65:
    print("you are not so old yet")
else:
    print("you are OLD, let's keep you younger:", age)
    while age > 65:
        print("your current age is: ", age)
        age = age - 1
    print("I told you, now you are: ", age)


# create dictionaries dinamically

dic = {"name": "Pepe", "Id": 1, "age": 34}
print(dic["age"])

dictio = {}

dictio["name"] = input("Insert name:")
print(dictio)

dictio["age"] = input("Insert age:")
print(dictio)

## print list elements

list1 = [1, 2, 4, 7.908, 5, 0]

print(list1)

print(list1[0])

print(len(list1))

# with while:

i = 0

while i < len(list1):
    print(list1[i])
    i = i + 1

# with for: MUCH MORE EASIER

for n in list1:
    print("RESPONSE IS ", n * 2)

# SUM numbers:
j = 0

for h in range(1, 6, 2):  ## TILL 6-1!!
    j = j + h

print(j)

# SUM USING WHILE:
j = 0
h = 1

while h < 6:
    j = j + h
    h = h + 2
print(j)

# same as before, but don't want some elements to be printed

j = 0
h = 1

while h < 7:
    if h != 3:
        j = j + h  # j=1
    h = h + 1  # h=

print(j)

# with CONTINUE, BREAK

j = 0
h = 1

while h < 7:
    if h == 3:
        h = h + 1
        continue  # starts another bucle iteration, ignoring above, but h needs to be incremented
    if h == 4:
        break  # it will do from 1 to 3, 4 will break, regardless while condition
    j = j + h
    h = h + 1

print(j)

######################################### Create a list of dictionaries

list_of_dicts = []

dic1 = {"name": "Pepe", "Id": 1, "age": 34}
dic2 = {"name": "Juan", "Id": 2, "age": 19}
dic3 = {"id": 56, "dog": True}
list_of_dicts.append(dic1)
list_of_dicts.append(dic2)
list_of_dicts.append(dic3)
print(list_of_dicts)

with open("example.txt", "w") as f:
    for items in list_of_dicts:
        f.writelines(items)
## this only saves item-key, not value

with open("output.txt", "w") as f:
    for item in list_of_dicts:
        f.write(str(item) + "\n")  ## this saves the whole line, adding ENTER

import json

with open("output.json", "w") as f2:
    json.dump(list_of_dicts, f2)  ## this creates JSON file

with open("output.json", "r") as f:
    print(json.load(f))  ## this prints back the created JSON

dic = {"append1": "Pepe", "append2": 1, "append3": 34}

## append JSON file: you need to save current JSON into a var, append, then write:

with open("output.json", "r") as f:
    data = json.load(f)

print(data)
data.append(dic)
print(data)
with open("output.json", "w") as f2:
    json.dump(data, f2)

## consider how to approach list elements: index-key:
print(data[2])
print(data[2]["dog"])

## Using lambda with map:

numbers = [1, 2, 3, 4]
double_numbers = map(lambda x: x * 2, numbers)
print(list(double_numbers))

## another way, with loop:
double_numbers2 = []
for item in numbers:
    double_numbers2.append(item * 2)

print(double_numbers2)  ## item is the value-element, not index

## filter only even numbers:

even = list(map((lambda x: x * 2), list(filter(lambda x: x % 2 == 1, numbers))))
print(even)  ## filters on CONDITION- only pick even from numbers

######## Sorting list:

list_sort = [4, 7, 3, 9, 0]
list_sort2 = ["apple", "orange", "banana", "lemon", "clementine"]

print(list_sort.sort())
print(list_sort2.sort())
# OR:
print(sorted(list_sort))

print(list_sort)
print(list_sort2)

## Reverse list:
list1 = [1, 2, 3, 4]
reverse = list1.reverse()  ## This actually upgrades original list1 to reverse
# OR:
reverse2 = list1[::-1]

print(list1)
