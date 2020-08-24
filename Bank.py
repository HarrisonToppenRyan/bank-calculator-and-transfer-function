class BankAccount:
    money   = None
    user    = None
    intrest = None

    def __init__(self, money, user, interest):
        self.money   = money
        self.user    = user
        self.intrest = interest

    def deposit(self, amount):
        self.money = self.money + amount
    
    def withdraw(self, amount):
        self.money = self.money - amount

    def transfer(self, amount, other):
        if self.money - amount <= 0:
            raise ValueError("Transfer cannot leave account negitive.")

        self.withdraw(amount)
        other.deposit(amount)

    def addIntrest(self):
        self.money = (self.money * self.intrest) + self.money
    

testAccount  = BankAccount(100, "test",  0.02)
testAccount2 = BankAccount(200, "test2", 0.02)

try:
    testAccount.transfer(10, testAccount2)
except:
    print("transfer error!")

print(testAccount.money)
print(testAccount2.money)