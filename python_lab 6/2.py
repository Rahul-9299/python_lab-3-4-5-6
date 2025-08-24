# Base class
class Animal:
	def speak(self):
		print("Animal makes a sound")

# Derived class
class Dog(Animal):
	def speak(self):
		print("Dog barks")

# Instantiate Dog and call speak()
dog = Dog()
dog.speak()
