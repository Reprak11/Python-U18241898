class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1
        self._reduce()

    def show(self):
        if self.nr == 0:
            print(0)
        else:
            print(f'{self.nr}/{self.dr}')

    def __str__(self):
        return f'{self.nr}/{self.dr}'

    def __repr__(self):
        return f'Fraction({self.nr},{self.dr})'

    def __mul__(self, other):
        if isinstance(other,int):
            other = Fraction(other)
        f = Fraction((self.nr * other.nr),(self.dr * other.dr))
        f._reduce() 
        return f

    def __add__(self, other):
        if isinstance(other,int):
            other = Fraction(other)
        f = Fraction(((self.nr * other.dr)+(other.nr * self.dr)),(self.dr * other.dr))
        f._reduce()
        return f

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other,int):
            other = Fraction(other)
        f = Fraction(((self.nr * other.dr)-(other.nr * self.dr)),(self.dr * other.dr))
        f._reduce()
        return f

    def __eq__(self, other):
        return (self.nr * other.dr) == (other.nr * self.dr)

    def __lt__(self,other):
        return (self.nr * other.dr) < (other.nr * self.dr)

    def __le__(self, other):
        return (self.nr * other.dr) <= (other.nr * self.dr)
    @staticmethod
    def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x>y else x
        s = smaller
        while s>0:
            if x%s==0 and y%s==0:
                break
            s-=1
        return s

    def _reduce(self):
        h = Fraction.hcf(self.nr, self.dr)
        if h == 0:
            return
        self.nr //= h
        self.dr //= h

f1 = Fraction(2,3)
f2 = Fraction(3,4)

f3 = f1 + f2
f4 = f1 - f2
f5 = f1 * f2
f3.show()
f4.show()
f5.show()

f6 = Fraction(2,3)
f7 = Fraction(2,3)

# Comparison methods
print(f6 == f7)
print(f1 < f2)
print(f1 <= f2)

# String methods
print(f1)

#Reverse methods
print(3 + f1)
