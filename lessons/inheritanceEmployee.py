from inheritancePerson import Person

class Employee(Person):
    def __init__(self, name, age, address, phone, salary,office_address, office_phone):
        super().__init__(name, age, address, phone)
        self.salary = salary
        self.office_address = office_address
        self.office_phone = office_phone

    def calculate_tax(self):
        return 0 if self.salary < 5000 else self.salary * 0.05

    def contact_details(self):
        print(self.address, self.phone, self.office_address, self.office_phone)

emp = Employee('Jack', 30, 'Tijuana', '93829', 8000, "Ensenada", '91112')

print(emp.name, emp.age, emp.address, emp.phone)
emp.greet()
print(emp.is_adult())
emp.contact_details()


# print(isinstance(emp, Employee))
# print(isinstance(emp, Person))
# print(issubclass(Employee, Person))

print(emp.salary, emp.office_address)
print(emp.calculate_tax())
