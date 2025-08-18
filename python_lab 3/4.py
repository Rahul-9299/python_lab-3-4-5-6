def book_info(title, author, year):
    print(f"Title: {title}\nAuthor: {author}\nYear: {year}")

# Demonstration with keyword arguments in different orders
book_info(title="1984", author="George Orwell", year=1949)
book_info(author="J.K. Rowling", year=1997, title="Harry Potter and the Philosopher's Stone")
book_info(year=2003, title="The Da Vinci Code", author="Dan Brown")
