class Bank_Account:
    def __init__(self, name,balance=0):
        self.name=name
        self.balance=balance
    
    def display(self):
        print(self.name, self.balance)
    
    def withdraw(self,amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount


account1 = Bank_Account('Jorge')
account1.deposit(350)
account1.withdraw(50)
account1.display()

account2 = Bank_Account('Raul',1000)
account2.display()