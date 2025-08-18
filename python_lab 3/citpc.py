
# Complete solution for the Car class task
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

    def __str__(self):
        return f"Car({self.make}, {self.model}, {self.year})"

# Create two Car objects
car1 = Car("Mahindra", "Scorpio", 2011)
car2 = Car("Toyota", "Corolla", 2018)

# Call display_info for each object
car1.display_info()
car2.display_info()

# Print string representation
print(car1)
print(car2)