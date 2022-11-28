class Product:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def display(self):
        print(self._x,self._y)
    
    @property #Get method
    def valueX(self):
        return self._x

    @valueX.setter #Set method
    def valueX(self,value):
        self._x=value

    @valueX.deleter
    def valueX(self):
        print('Value X deleted')

    @property
    def valueY(self):
        return self._y

    @valueY.setter
    def valueY(self,value):
        self._y = value
        
    @valueY.deleter
    def valueY(self):
        print('Value Y deleted')

p = Product(12,24)
print(p.valueX + 5)
p.value = 100
print(p.valueX)
del p.valueX