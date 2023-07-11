class Bank:
    def __init__(self, balance, name, account_number):
        self.balance = balance
        self.name = name
        self.account_number = account_number
    
    def withdraw(self, money):
        self.balance-=money
    
    def deposit(self, money):
        self.balance+=money
    
    def print_balance(self):
        print(self.balance)