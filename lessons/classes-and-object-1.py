from queue import PriorityQueue
from time import perf_counter


class Person:
    def set_details(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print('Hello from the object', self)
        self.greeting()
    def greeting(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old")


p1 = Person()
p2 = Person()


#print(id(Person))
#print(type(p1), id(p1))
#print(type(p2), id(p2))

p1.set_details('Reprak',27)
p1.display()
#p1.greeting()


p2.set_details('Reynaldo', 28)
p2.display()
#p2.greeting()

