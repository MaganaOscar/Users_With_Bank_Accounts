class BankAccount:
    # don't forget to add some default values for these parameters!
    accounts = []
    def __init__(self, int_rate, balance): 
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        self.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if(self.balance < amount):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        # your code here
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        # your code here
        self.balance = self.balance + self.balance*self.int_rate
        return self
    @classmethod
    def all_balances(cls):
        print(f"Accounts: {len(cls.accounts)}")
        for account in cls.accounts:
            print(f"Balance: {account.balance}\nInterest Rate: {account.int_rate}")

class User:
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    accounts = {}
    # now our method has 2 parameters!
    def __init__(self, name, email_address, acc_Name, int_rate = 0.01, balance = 0):
    	# we assign them accordingly
        self.name = name
        self.email = email_address
    	# the account balance is set to $0
        self.account = BankAccount(int_rate, balance)
        self.accounts[acc_Name] = self.account
    def make_withdrawal(self, amount, acc_Name):
        # self.account.balance -= int(amount)
        if self.accounts[acc_Name].balance < amount:
            print("Insufficient funds: Charging $5 fee")
            self.accounts[acc_Name].balance -= 5
        self.accounts[acc_Name].balance -= int(amount)
        return self
    def make_deposit(self, amount, acc_Name):
        # self.account.balance += amount
        self.accounts[acc_Name].balance += amount
        return self
    def display_user_balance(self, acc_Name):
        print(f"User: {self.name}, Account: {acc_Name}, Balance: ${self.accounts[acc_Name].balance}")
        return self
    def transfer_money(self, other_user, amount, acc_Name, otherAccName):
        self.accounts[acc_Name].balance -= amount
        other_user.accounts[otherAccName].balance += amount
        return self
    def newAccount(self, acc_Name, int_rate = 0.01, balance = 0):
        self.account = BankAccount(int_rate, balance)
        self.accounts[acc_Name] = self.account

account1 = User('Bob', 'bob@email.com', 'Savings')
account1.display_user_balance('Savings')
account1.make_deposit(100, 'Savings')
account1.display_user_balance('Savings')
account2 = User('Tim', 'tim@email.com', 'Savings')
account2.display_user_balance('Savings')
account1.newAccount('Checkings')
account1.display_user_balance('Checkings')