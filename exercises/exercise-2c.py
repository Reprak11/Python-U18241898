class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1

    def show(self):
        if self.nr == 0:
            print(0)
        else:
            print(f'{self.nr}/{self.dr}')

    def multiply(self, other):
        if isinstance(other,int):
            other = Fraction(other)
        return Fraction((self.nr * other.nr),(self.dr * other.dr))

    def add(self, other):
        if isinstance(other,int):
            other = Fraction(other)
        return Fraction(((self.nr * other.dr)+(other.nr * self.dr)),(self.dr * other.dr))

f1 = Fraction(2,3)
f1.show()
f2 = Fraction(2,-3)
f2.show()
f3 = Fraction(-5,-6)
f3.show()

fm = f1.multiply(f2)
fm.show()

fs = f1.add(f2)
fs.show()
