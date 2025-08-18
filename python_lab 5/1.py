class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

    def update_price(self, new_price):
        self.price = new_price

book1 = Book("The Python Programming", "Ram Parsad", 299.99)
book1.display_info()
print("\nUpdating price...\n")
book1.update_price(349.99)
book1.display_info()
