class Bank:
    balance = 1000
    def __init__(self,accountno):
        self.accountno=accountno
        print("Initially the account number",self.accountno,"has balance of rs",Bank.balance)

    def credit(self,amount):
        self.balance = self.balance + amount
        print("Amount credited +",amount,"\nAvailable balance is :",self.balance)

    def debited(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Amount debited -:",amount,"\nAvailable balance is :",self.balance)
        else:
            print("Check balance")
    
    def check_balance(self):
        print("Available balance is :",self.balance)

b1 = Bank("12345678SBI80808")
b1.credit(1000)
b1.debited(500)
b1.check_balance()
        