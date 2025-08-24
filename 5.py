
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Employee(Person):
	def __init__(self, name, age, employee_id, salary):
		super().__init__(name, age)
		self.employee_id = employee_id
		self.salary = salary

	def display_employee(self):
		print(f"Name: {self.name}")
		print(f"Age: {self.age}")
		print(f"Employee ID: {self.employee_id}")
		print(f"Salary: {self.salary}")

emp = Employee("Rahul", 30, "E123", 50000)
emp.display_employee()
