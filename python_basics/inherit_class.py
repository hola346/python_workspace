from classes import calcu  # name of file py containing class


class pare(calcu):
    num2 = 200

    # you need to define constructor here, even for the child to run
    def __init__(self, a, b, c):
        calcu.__init__(self, a, b)
        self.c = c

    def getDataComplete(self):
        return self.num2 + self.number + self.summm() + self.c


obj3 = pare(11, 8, 6)
print(obj3.getDataComplete())
