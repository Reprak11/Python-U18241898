class Employee:
    def __init__(self, name, password, salary):
        self.name = name
        self.password = password
        self.salary =  salary

    #Name only read only 
    @property
    def name(self):
        return self._name
    
    #Password is only write only
    @property
    def password(self):
        raise AttributeError('Password not readable')
    
    @password.setter
    def password(self, new_password):
        self._password = new_password

    #Salary is read/write
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

e = Employee('Jill','1234ABCD',5000)