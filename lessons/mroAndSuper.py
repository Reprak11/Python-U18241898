class Person:
    def greet(self):
        print('I am a Person')

class Teacher(Person):
    def greet(self):
        super().greet()
        print('I am a Teacher')

class Student(Person):
    def greet(self):
        super().greet()
        print('I am a Student')

class TeachingAssistant(Teacher, Student): # Classes will be inheritance in the order that the parent classess are defined
    def greet(self):
        super().greet() # This super follows MRO
        print('I am a Teacher Assistant')

x = TeachingAssistant()
x.greet()
