class Bank:
    def __init__(self, name: str, account_number: int, balance: float or int = 0):
        self.balance = balance
        self.name = name
        self.account_number = account_number

    def withdraw(self, money: int or float):
        if self.balance <= money:
            raise ValueError("Not enough money to withdraw.")
        else:
            self.balance -= money
            print(f"Successfully withdrew {money} from account.")
            return self.balance

    def deposit(self, money: int or float):
        self.balance += money
        print(f"Successfully deposited {money} in account.")
        return self.balance

    def print_balance(self):
        print(f"Balance: {self.balance}")
        return self.balance
