from OopsDemo import Calculator


class Child (Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__ (self, 10, 9)

    def getcompeletedat(self):
        return self.num2 + self.num + self.submition()


obj = Child()
obj.getData()
print(obj.getcompeletedat())