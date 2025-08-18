class Bank_Account:
    def __init__(self,acc_holder, acc_number, balance):
        self.acc_holder = acc_holder
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self, amt):
        self.balance = self.balance + amt
    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - amt
    def show_balance(self):
        print(f"Account Holder: {self.acc_holder}")
        print(f"Account Number: {self.acc_number}")
        print(f"Balance: {self.balance}")
ob1 = Bank_Account("Ram", "00984638262", 10000)
ob1.show_balance()
print("\nWithdrawing 2000...\n")
ob1.withdraw(2000)
ob1.show_balance()
print("\nDepositing 4000...\n")
ob1.deposit(4000)
ob1.show_balance()