accounts = {}

def account_exists(user_id):
    return user_id in accounts

def create_account(user_id):
    if account_exists(user_id):
        print("Account already exists.")
    else:
        accounts[user_id] = {'balance': 0}
        print(f"Account created for user {user_id}")

def check_balance(user_id):
    if account_exists(user_id):
        balance = accounts[user_id]['balance']
        print(f"Balance for user {user_id}: {balance}")
    else:
        print("Account does not exist.")

def deposit(user_id, amount):
    if account_exists(user_id):
        accounts[user_id]['balance'] += amount
        print(f"Deposited {amount} into account of user {user_id}")
        check_balance(user_id)
    else:
        print("Account does not exist.")

def withdraw(user_id, amount):
    if account_exists(user_id):
        if accounts[user_id]['balance'] >= amount:
            accounts[user_id]['balance'] -= amount
            print(f"Withdrew {amount} from account of user {user_id}")
            check_balance(user_id)
        else:
            print("Insufficient balance.")
    else:
        print("Account does not exist.")

def delete_account(user_id):
    if account_exists(user_id):
        del accounts[user_id]
        print(f"Account of user {user_id} deleted.")
    else:
        print("Account does not exist.")

while True:

    choice = input("HELLO AKIRES: ")

    if choice == "1":
        user_id = input("UD: ")
        create_account(user_id)
    elif choice == "2":
        user_id = input("Enter user ID: ")
        check_balance(user_id)
    elif choice == "3":
        user_id = input("Enter user ID: ")
        amount = float(input("Enter deposit amount: "))
        deposit(user_id, amount)
    elif choice == "4":
        user_id = input("Enter user ID: ")
        amount = float(input("Enter withdrawal amount: "))
        withdraw(user_id, amount)
    elif choice == "5":
        user_id = input("Enter user ID: ")
        delete_account(user_id)
    elif choice == "6":
        print("Thank you for using Simple Banking System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
