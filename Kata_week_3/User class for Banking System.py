class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
        
    def withdraw (self, money_withdrawn):
        if money_withdrawn > self.balance:
            raise ValueError("Not enough balance")
        else:
            self.balance -= money_withdrawn 
        return (self.name + " has " + str(self.balance) + ".")

    def check (self, other_user, money):
        if other_user.balance < money:
            raise ValueError("Not enough balance for transaction")
        elif other_user.checking_account == False:
            raise ValueError("No checking account")
        else: 
            self.balance += money
            other_user.balance -= money
            return (self.name + " has " + str(self.balance) + " and " + other_user.name + " has " + str(other_user.balance) + ".")
    
    def add_cash (self, money):
        self.balance += money
        return (self.name + " has " + str(self.balance) + ".")
    

