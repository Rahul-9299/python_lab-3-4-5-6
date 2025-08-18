import time

def add_customer(filename):
    try:
        name = input("Enter customer name: ")
        acc_num = input("Enter account number: ")
        balance = float(input("Enter initial balance: "))
        with open(filename, 'a') as f:
            f.write(f"{name},{acc_num},{balance}\n")
        print("Customer added.")
    except Exception as e:
        print(f"Error: {e}")

def view_customers(filename):
    try:
        with open(filename, 'r') as f:
            customers = f.readlines()
            if not customers:
                print("No customers found.")
            else:
                print("Customers:")
                for c in customers:
                    name, acc, bal = c.strip().split(',', 2)
                    print(f"Name: {name}, Account: {acc}, Balance: {bal}")
    except FileNotFoundError:
        print("Customer file not found.")
    except Exception as e:
        print(f"Error: {e}")

def log_transaction(filename, acc_num, amount, t_type):
    try:
        with open(filename, 'a') as f:
            ts = time.strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"{ts},{acc_num},{amount},{t_type}\n")
    except Exception as e:
        print(f"Error logging transaction: {e}")

def update_balance(cust_file, acc_num, amount, t_type, trans_file):
    try:
        updated = False
        lines = []
        with open(cust_file, 'r') as f:
            lines = f.readlines()
        with open(cust_file, 'w') as f:
            for line in lines:
                name, acc, bal = line.strip().split(',', 2)
                if acc == acc_num:
                    bal = float(bal)
                    if t_type == 'deposit':
                        bal += amount
                        print(f"Deposited {amount}. New balance: {bal}")
                    elif t_type == 'withdrawal':
                        if bal >= amount:
                            bal -= amount
                            print(f"Withdrew {amount}. New balance: {bal}")
                        else:
                            print("Insufficient funds.")
                            f.write(line)
                            continue
                    updated = True
                    f.write(f"{name},{acc},{bal}\n")
                    log_transaction(trans_file, acc, amount, t_type)
                else:
                    f.write(line)
        if not updated:
            print("Account not found.")
    except FileNotFoundError:
        print("Customer file not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    cust_file = 'customers.txt'
    trans_file = 'transactions.txt'
    while True:
        print("\nBanking System CLI")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_customer(cust_file)
        elif choice == '2':
            view_customers(cust_file)
        elif choice == '3':
            acc = input("Enter account number: ")
            try:
                amt = float(input("Enter deposit amount: "))
                update_balance(cust_file, acc, amt, 'deposit', trans_file)
            except ValueError:
                print("Invalid amount.")
        elif choice == '4':
            acc = input("Enter account number: ")
            try:
                amt = float(input("Enter withdrawal amount: "))
                update_balance(cust_file, acc, amt, 'withdrawal', trans_file)
            except ValueError:
                print("Invalid amount.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
