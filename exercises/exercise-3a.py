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