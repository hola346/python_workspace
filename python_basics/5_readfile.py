textfile = open("file.txt", mode="r")

# print(textfile.read()) --> (3), print 3 first letters

# print(textfile.read(-3))

print(textfile.readline())  # reads 1st line
print(textfile.readline())  # reads next line
# print("Interpretor" in textfile)

for i in range(1, 6):
    print(textfile.readline())

# another way, if we don't know how many lines, read till the end - ""

line = textfile.readline()
while line != "":
    print(line)
    line = textfile.readline()  # read next line

line = textfile.readlines()
print(line)

for line in textfile.readlines():
    print(line)

print(line.__len__())
print(line[2])
print(line[-1])
print(line.__sizeof__())
print(type(line))  # it's a list

textfile.close()  # good practice, once finishing reading, close it.
