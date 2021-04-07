#class of user
class user:
    def __init__(self, name, balance):
        self.name = name
        #create array and store bankAccount in it.
        self.bankAccounts = {}
    def openAccount(self, name, rate, balance):
        self.bankAccounts[name] = BankAccount(rate, balance)
        pass

class BankAccount:
    def __init__(self, int_rate, balance): # don't forget to add some default values for these parameters!
        self.int_rate = int_rate
        self.balance = balance 
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def displayAccountInfo(self):
        print(self.balance)
        return self
    def yieldInterest(self):
        self.balance = self.balance*self.int_rate + self.balance
        return self


#Three instances of the class user
fredrick = user("fredrick", 91)
william = user("william", 90)
micheal = user("words",80)
#chain calling a list of commands.
fredrick.openAccount("Checking", .02, 800)
fredrick.bankAccounts["Checking"].deposit(740)
fredrick.bankAccounts["Checking"].displayAccountInfo()
print(fredrick.bankAccounts)


