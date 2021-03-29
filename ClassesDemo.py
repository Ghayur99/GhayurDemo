class Calculater:
    num = 100
    Num2 = 200

    def __init__(self):
        print("constructor")

    def Sum(self, a,b):
        return a + b

Obj = Calculater()
print(Obj.Sum(5,6))
print(Obj.Sum(15,20))

