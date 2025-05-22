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
    users = {}  # Dictionary to store user accounts
    current_user = None

    while True:
        if current_user is None:
            name = input("Enter account holder name: ").strip()
            if name in users:
                current_user = users[name]
                print(f"Welcome back, {name}!")
            else:
                create = input("User not found. Create new account? (yes/no): ").strip().lower()
                if create == 'yes':
                    new_account = Account(name)
                    users[name] = new_account
                    current_user = new_account
                    print(f"Account created for {name}.")
                else:
                    continue

        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Add New User")
        print("5. Switch User")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            try:
                amt = float(input("Enter amount to deposit: "))
                current_user.deposit(amt)
            except ValueError:
                print("Invalid amount.")
        elif choice == '2':
            try:
                amt = float(input("Enter amount to withdraw: "))
                current_user.withdraw(amt)
            except ValueError:
                print("Invalid amount.")
        elif choice == '3':
            current_user.display()
        elif choice == '4':
            name = input("Enter new account holder name: ").strip()
            if name in users:
                print("User already exists.")
            else:
                users[name] = Account(name)
                print(f"Account created for {name}.")
        elif choice == '5':
            name = input("Enter account holder name to switch: ").strip()
            if name in users:
                current_user = users[name]
                print(f"Switched to user: {name}")
            else:
                print("User does not exist.")
        elif choice == '6':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid option. Please choose between 1–6.")

if __name__ == "__main__":
    main()
