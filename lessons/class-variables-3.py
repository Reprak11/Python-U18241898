class Account:
    rate = 5

a1 = Account()
a2 = Account()

print(a1.rate, a2.rate, Account.rate)

Account.rate = 10

print(a1.rate, a2.rate, Account.rate)

a1.rate = 7 # This statement don't change the class variable, it creates a new instance variable

print(a1.rate, a2.rate, Account.rate)