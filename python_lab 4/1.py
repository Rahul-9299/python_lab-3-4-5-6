def add_contact(filename):
    try:
        count = int(input("How many contacts do you want to add? "))
        with open(filename, 'a') as f:
            for i in range(count):
                print(f"\nContact {i+1}:")
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                f.write(f"{name},{phone}\n")
        print(f"{count} contact(s) added.")
    except ValueError:
        print("Invalid number entered.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def view_contacts(filename):
    try:
        with open(filename, 'r') as f:
            contacts = f.readlines()
            if not contacts:
                print("No contacts found.")
            else:
                print("Contacts:")
                for contact in contacts:
                    name, phone = contact.strip().split(',', 1)
                    print(f"Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print("Contact file not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def search_contact(filename):
    search_name = input("Enter name to search: ").lower()
    found = False
    try:
        with open(filename, 'r') as f:
            for contact in f:
                name, phone = contact.strip().split(',', 1)
                if search_name in name.lower():
                    print(f"Found: Name: {name}, Phone: {phone}")
                    found = True
        if not found:
            print("Contact not found.")
    except FileNotFoundError:
        print("Contact file not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    filename = 'contacts.txt'
    while True:
        print("\nContact Book CLI")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_contact(filename)
        elif choice == '2':
            view_contacts(filename)
        elif choice == '3':
            search_contact(filename)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()