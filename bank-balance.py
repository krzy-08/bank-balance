class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def show_balance(self):
        return f"{self.name}'s balance is ${self.balance}"
    
    def deposit_amount(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insuffucient funds"
        else:
            self.balance -= amount
            return f"Withdraw ${amount}. New balance: ${self.balance}"

account = BankAccount("John", 100)
account.deposit_amount(1000)
print(account.show_balance())
account.withdraw(200)
account.withdraw(500)
print(account.show_balance())