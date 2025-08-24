
class BankAccount:
	def __init__(self, account_number, balance=0):
		self.__account_number = account_number
		self.__balance = balance

	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			print(f"Deposited: {amount}")
		else:
			print("Deposit amount must be positive.")

	def withdraw(self, amount):
		if amount > 0:
			if self.__balance - amount >= 0:
				self.__balance -= amount
				print(f"Withdrawn: {amount}")
			else:
				print("Insufficient balance.")
		else:
			print("Withdrawal amount must be positive.")

	def get_account_details(self):
		print(f"Account Number: {self.__account_number}")
		print(f"Balance: {self.__balance}")

account = BankAccount("1234567890", 1000)
account.get_account_details()
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  
account.get_account_details()
