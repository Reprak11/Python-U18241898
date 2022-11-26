class Product:
    def __init__(self):
        self.data1 = 10
        self._data2 = 20
    def methodA(self):
        print('Method A')
    def __methodB(self):
        print('Method B')

p = Product()
print(p.data1,p._data2)
p.methodA()
p._Product__methodB()