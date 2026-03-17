class calcu:
    number = 100

    def __init__(
        self, a, b
    ):  # constructor: for initializing vars, work internally with internal vars and methods
        self.a = a
        self.b = b

    def operator(self):  # normally self is used ()
        print("this is operator message")

    def summing(
        self, elem1, elem2
    ):  # class work internally with params with self.param
        self.elem1 = elem1
        self.elem2 = elem2
        print("the sum of elements is ", self.elem1 + self.elem2 + self.number)
        # this works, but the most OK thing is to ini params on constructor, see next method

    def summm(
        self,
    ):  # don't need to def params here, as they come from constructor - init
        return self.a + self.b + self.number


# Main reason for a constructor - init is you may have several objects instanced to same class
# so all values-vars within every object are distinct and noted for every object

obj = calcu(77, 88)  # normally () is used

print(obj.number)
obj.operator()

obj1 = calcu(44, 55)
obj1.summing(12, 3)

obj2 = calcu(
    5, 6
)  # you pass your params in class def, so they will be used within class
obj2.summm()
