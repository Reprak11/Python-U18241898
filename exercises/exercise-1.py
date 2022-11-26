class Bank_Account:
    def set_details(self, name):
        self.name=name
        self.balance=0
    def display(self):
        print(self.name, self.balance)
    def withdraw(self,amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount


account1 = Bank_Account()
account1.set_details('Jorge')
account1.deposit(350)
account1.withdraw(50)
account1.display()

account2 = Bank_Account()
account2.set_details('Raul')
account2.deposit(1000)
account2.display()