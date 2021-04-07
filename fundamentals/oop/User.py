#class of user
class user:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def makeDeposit(self, amount):
        self.balance += amount
        return self

    def makeWithdrawal(self, amount):
        self.balance -= amount
        return self

    def displayUserBalance(self):
        print(self.balance,"$")
        return self
    
    def transferMoney(self, amount, user):
        self.balance -= amount
        user.balance += amount
        return self

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
micheal.makeDeposit(800).makeDeposit(800).makeDeposit(800).makeWithdrawal(1200).transferMoney(200,fredrick).displayUserBalance()
william.makeWithdrawal(20).makeWithdrawal(20).makeWithdrawal(20).makeDeposit(90).displayUserBalance()
fredrick.makeDeposit(90).makeDeposit(90).makeWithdrawal(90).makeWithdrawal(90).displayUserBalance()

fredrickBankAccount = BankAccount(.01,800)
fredrickBankAccount.deposit(200).deposit(200).deposit(200).withdraw(900).yieldInterest().displayAccountInfo()
williamBankAccount = BankAccount(.01,800)
williamBankAccount.deposit(800).deposit(350).withdraw(250).withdraw(100).withdraw(100).withdraw(100).yieldInterest().displayAccountInfo()
