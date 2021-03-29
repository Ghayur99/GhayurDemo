from OopsDemo import Calculator


class Child2(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,7,10)


    def Addition(self):
        return self.num2 + 300 + self.submition() + self.num

obj = Child2()
print(obj.Addition())
print(obj.submition())

