#class of user
class user:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        return self
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
#Three instances of the class user
fredrick = user("fredrick", 91)
william = user("william", 90)
micheal = user("words",80)
#chain calling a list of commands.
micheal.makeDeposit(800).makeDeposit(800).makeDeposit(800).makeWithdrawal(1200).transferMoney(200,fredrick).displayUserBalance()
william.makeWithdrawal(20).makeWithdrawal(20).makeWithdrawal(20).makeDeposit(90).displayUserBalance()
fredrick.makeDeposit(90).makeDeposit(90).makeWithdrawal(90).makeWithdrawal(90).displayUserBalance()


