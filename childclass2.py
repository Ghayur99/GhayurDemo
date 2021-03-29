from OopsDemo import Calculator


class ChildClass (Calculator):
    NUM2 = 500

    def __init__(self):
        Calculator.__init__(self, 70, 11)

    def addition(self):
        return self.NUM2 + self.num + 300 + self.submition()


obj = ChildClass()
print(obj.addition())
