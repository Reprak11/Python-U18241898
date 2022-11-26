class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print('Hello from the object', self)
        self.greeting()
    def greeting(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old")


p1 = Person('Reprak',27)
p2 = Person('Reynaldo', 28)

p1.display()
p2.display()
