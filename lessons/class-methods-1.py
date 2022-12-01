class MyClass:
    a = 5

    def __init__(self, x):
        self._x = x

    def method1(self):
        print(self.x)

    @classmethod
    def method2(cls):   #cls is the first instance parameter, just like self
        print(cls.a)

MyClass.method2()
