
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

class Contact:
    def __init__(self, person, address):
        self.person = person
        self.address = address

    def display_contact(self):
        print(f"Name: {self.person.name}")
        print(f"Age: {self.person.age}")
        print(f"Address: {self.address.street}, {self.address.city}, {self.address.zipcode}")

person1 = Person("Alice", 28)
address1 = Address("123 Main St", "Springfield", "12345")
contact1 = Contact(person1, address1)
contact1.display_contact()
