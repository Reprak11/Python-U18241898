class Person:
    a = 5
    def greet(self):
        print('I am a Person')

class Teacher(Person):
    def greet(self):
        print('I am a Teacher')

class Student(Person):
    def greet(self):
        print('I am a Student')

class TeachingAssistant(Teacher, Student): # Classes will be inheritance in the order that the parent classess are defined
    def greet(self):
        print('I am a Teacher Assistant')

x = TeachingAssistant()
x.greet()
print(x.a)
#help(TeachingAssistant)
print(TeachingAssistant.mro())
print(x.__class__.__mro__)