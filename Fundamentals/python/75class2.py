class Bank:

    def __init__(self,acc_no,initial_bal,amount,balance):
        self.acc_no=acc_no
        self.initial_bal=initial_bal
        self.amount=amount
        self.balance = balance

    def create_account(self,acc_no,initial_bal=0):
        self.acc_no=acc_no
        self.initial_bal=initial_bal
        
    def make_deposite(self,acc_no,amount):
        self.acc_no=acc_no
        self.amount=amount
    def make_withdrawal(self,acc_no,amount):
        self.acc_no=acc_no
        self.amount=amount
    def check_balance(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance = balance

    def Bank(self):
        print("acc_no:",self.acc_no)
        print("initial_bal",self.initial_bal)

        print("amount:",self.amount)
        print("balance:",self.balance)

B1 = Bank('234455666','0','1000000','50000')
B1.Bank()
    
