class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}, New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def display(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")


def main():
    print("Welcome to Virtual Height Bank!")
    users = {}
    current_user = None

    while True:
        if not current_user:
            name = input("Enter account holder name: ")
            if name in users:
                current_user = users[name]
            else:
                create = input("User not found. Create new account? (yes/no): ")
                if create.lower() == 'yes':
                    users[name] = Account(name)
                    current_user = users[name]
                    print(f"Account created for {name}.")
                else:
                    continue

        print("\n1. Deposit\n2. Withdraw\n3. Display Balance\n4. Add new user\n5. Switch user\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amt = float(input("Enter amount to deposit: "))
            current_user.deposit(amt)
        elif choice == '2':
            amt = float(input("Enter amount to withdraw: "))
            current_user.withdraw(amt)
        elif choice == '3':
            current_user.display()
        elif choice == '4':
            name = input("Enter new account holder name: ")
            if name in users:
                print("User already exists.")
            else:
                users[name] = Account(name)
                current_user = users[name]
                print(f"Account created for {name}.")
        elif choice == '5':
            name = input("Enter account holder name to switch: ")
            if name in users:
                current_user = users[name]
                print(f"Switched to user: {name}")
            else:
                print("User does not exist.")
        elif choice == '6':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
        