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
