class MyClass():
    a = 5
    def __init__(self,x):
        self.x = x

    def method1(self):
        print(self.x)

    @classmethod
    def method2(cls):
        print(cls.a)

    @staticmethod # Note this methods doesn't need first special parameters
    def method3(m,n):
        return m + n

mc = MyClass(2)

mc.method1()
mc.method2()
print(mc.method3(4, 5))