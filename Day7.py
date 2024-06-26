import random

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        user_id = random.randint(1000, 9999)
        pin = int(input("Create your PIN: "))
        self.accounts[user_id] = {"pin": pin, "balance": 0.0}
        print("Your account ID is: ", user_id)

    def get_account(self, user_id):
        return self.accounts.get(user_id)

    def delete_account(self, user_id):
        if user_id in self.accounts:
            del self.accounts[user_id]
        else:
            print("Account not found")

class Account:
    def __init__(self, account_data):
        self.account_data = account_data

    def deposit(self, amount):
        self.account_data["balance"] += amount
        print("Deposit successful. New balance: ", self.account_data["balance"])

    def check_balance(self):
        print("Your balance: ", self.account_data["balance"])

    def withdraw(self, amount):
        if amount <= self.account_data["balance"]:
            self.account_data["balance"] -= amount
            print("Withdrawal successful. New balance: ", self.account_data["balance"])
        else:
            print("Insufficient balance")

def main():
    bank = Bank()
    while True:
        choice = input("Enter your choice:\n1. Create account\n2. Deposit\n3. Check balance\n4. Withdraw\n5. Delete account\n6. Exit\n")
        if choice == "1":
            bank.create_account()
        elif choice == "2":
            user_id = int(input("Enter your account ID: "))
            pin = int(input("Enter your PIN: "))
            account = bank.get_account(user_id)
            if account and account["pin"] == pin:
                amount = float(input("Enter amount to deposit: "))
                account_obj = Account(account)
                account_obj.deposit(amount)
            else:
                print("Invalid PIN or Account not found")
        elif choice == "3":
            user_id = int(input("Enter your account ID: "))
            pin = int(input("Enter your PIN: "))
            account = bank.get_account(user_id)
            if account and account["pin"] == pin:
                account_obj = Account(account)
                account_obj.check_balance()
            else:
                print("Invalid PIN or Account not found")
        elif choice == "4":
            user_id = int(input("Enter your account ID: "))
            pin = int(input("Enter your PIN: "))
            account = bank.get_account(user_id)
            if account and account["pin"] == pin:
                amount = float(input("Enter amount to withdraw: "))
                account_obj = Account(account)
                account_obj.withdraw(amount)
            else:
                print("Invalid PIN or Account not found")
        elif choice == "5":
            user_id = int(input("Enter your account ID: "))
            pin = int(input("Enter your PIN: "))
            account = bank.get_account(user_id)
            if account and account["pin"] == pin:
                bank.delete_account(user_id)
            else:
                print("Invalid PIN or Account not found")
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
