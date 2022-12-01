class Book:
    x = 5

    def __init__(self):
        self.x = 100

    def display(self):
        print(self.x) 
        print(Book.x)

b = Book()

print(b.x, Book.x) #Python first check instance variable and then class variable ex. b.x = 5 as this is the instance variable
