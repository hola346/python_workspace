var = "Welcome to Python Programming"
print(var)

var = var + ", Rahul!"
print(var)

########################

age = 25
height = 5.9
favorite_color = "blue"

print("Age: ", age, " | Type: ", type(age))
print("Height: ", height, " | Type: ", type(height))
print("Favorite Color: ", favorite_color, " | Type: ", type(favorite_color))

###########################
##--> check 3rd one
person = ("Rahul", 25, 5.9)  # tuple, cannot be modified
print("Age:", person[1])

###########################

car = {"make": "Toyota", "model": "Camry", "year": 2020, "color": "Blue"}
print("Car model:", car["model"])

car["owner"] = "Rahul"  # update dictionary
print(car)

############################# IF

greeting = "Hello"

if greeting == "Hello":
    print("Hello there!")
    print("How can I assist you today?")
else:
    print("Greetings!")
print("Program has completed.")

#############################

b = 15

if b > 10:
    print("Number is greater than 10")
else:
    print("Number is 10 or less")
print("Comparison code is completed.")

##################################

numbers = [1, 4, 7, 10]

for num in numbers:
    print(num * 3)

#######################################

user = 22

if user >= 5 and user <= 11:
    print("Good Morning")
elif user >= 12 and user <= 17:
    print("Good Afternoon")
elif user >= 18 and user <= 21:
    print("Good Evening")
else:
    print("Good Night")
print("Greeting code has completed.")


################################################ CLASS - Constructor


class BasicCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Addition(self):
        print("Addition:", self.a, "+", self.b, "=", self.a + self.b)

    def Subtraction(self):
        print("Subtraction:", self.a, "-", self.b, "=", self.a - self.b)

    def Multiplication(self):
        print("Multiplication:", self.a, "*", self.b, "=", self.a * self.b)

    def Division(self):
        print("Division:", self.a, "/", self.b, "=", self.a / self.b)


calc = BasicCalculator(10, 5)
calc.Addition()
calc.Subtraction()
calc.Multiplication()
calc.Division()

############################################### FUNCTIONS


def GreetUser(username):
    print(
        "Hello, " + username + "! Welcome to the Python course."
    )  # NOTA: ++++ for less spaces, instead of ,


GreetUser("John")

###############################################


def CalculateAverage(num1, num2, num3):
    return (num1 + num2 + num3) / 3


print("The average of 10, 20 and 30 is", CalculateAverage(10, 20, 30))

################################################ READ FILE

file = open("file1.txt", "r")
print(file.read())
file.close()

#

with open("file1.txt", "r") as file:
    print(file.read())

###################################################COUNT LINES IN FILE

with open("file.txt", "r") as file1:
    i = 0
    for line in file1:
        print(file1.readline())
        i = i + 1
    print(i)

#
with open("file.txt", "r") as file1:
    x = len(file1.readlines())
    print("Total lines:", x)
# OR
with open("file.txt", "r") as file1:
    count = sum(1 for line in file1)
    print(f"Total number of lines: {count}")

############################################ items chart

ItemsInCart = 0


def add_to_cart(items_to_add):

    global ItemsInCart  ### to remember previous value each execution when incrementing

    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")

    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")

    # NOTE EXCEPTIONS: won't go running further the program

    ItemsInCart += items_to_add  ### <----------

    print(f"{items_to_add} items added. Total in cart: {ItemsInCart}")


add_to_cart(2)
add_to_cart(2)
add_to_cart(-11)
add_to_cart(1)
add_to_cart(1)
add_to_cart(-11)

############################################ CANNOT CHANGE TUPLE CONTENT

person = ("Rahul", 25, 5.9)
# Print the second element of the tuple
print(f"Age: {person[1]}")

# Attempt to change the name in the tuple (this will raise an error)
try:  ## note checking/test for a negative case - controlled error: try - except
    person[0] = "John"  # This will not work
except Exception as e:
    print(f"Error: {e} - Tuples are immutable.")

############################################
