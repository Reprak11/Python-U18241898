class Person:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    def greet(self):
        print(f'Hello, I am {self.name}')

    def is_adult(self):
        return self.age > 18

    def contact_details(self):
        print(self.address, self.phone)