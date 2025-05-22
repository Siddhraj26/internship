import json
import os

class User:
    def __init__(self, username, balance=0.0):
        self.username = username
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Current balance for {self.username}: ${self.balance:.2f}")

class BankSystem:
    def __init__(self, data_file="bank_data.json"):
        self.data_file = data_file
        self.users = self.load_users()
        self.current_user = None

    def load_users(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                raw_data = json.load(f)
                return {username: User(username, info['balance']) for username, info in raw_data.items()}
        return {}

    def save_users(self):
        data = {username: {"balance": user.balance} for username, user in self.users.items()}
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def create_user(self):
        username = input("Enter new username: ")
        if username in self.users:
            print("User already exists.")
        else:
            self.users[username] = User(username)
            self.save_users()
            print(f"User '{username}' created.")

    def switch_user(self):
        username = input("Enter username to switch to: ")
        if username in self.users:
            self.current_user = self.users[username]
            print(f"Switched to user: {username}")
        else:
            print("User not found.")

    def user_menu(self):
        while True:
            print(f"\n--- {self.current_user.username}'s Account ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Switch User")
            print("0. Logout")

            choice = input("Choose an option: ")

            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                self.current_user.deposit(amount)
                self.save_users()
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                self.current_user.withdraw(amount)
                self.save_users()
            elif choice == "3":
                self.current_user.check_balance()
            elif choice == "4":
                self.switch_user()
                if self.current_user:
                    continue
                else:
                    break
            elif choice == "0":
                self.current_user = None
                break
            else:
                print("Invalid option.")

    def main_menu(self):
        while True:
            print("\n--- Banking System ---")
            print("1. Create new user")
            print("2. Switch user")
            print("0. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.create_user()
            elif choice == "2":
                self.switch_user()
                if self.current_user:
                    self.user_menu()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")

# Run the banking system
if __name__ == "__main__":
    bank = BankSystem()
    bank.main_menu()
