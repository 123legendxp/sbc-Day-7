accounts = {}

def create_account(user_id):
    if user_id in accounts:
        print("Account already exists.")
    else:
        accounts[user_id] = 0
        print(f"Account created for user {user_id}")

def check_balance(user_id):
    balance = accounts.get(user_id)
    if balance is not None:
        print(f"Balance for user {user_id}: {balance}")
    else:
        print("Account does not exist.")

def deposit(user_id, amount):
    if user_id in accounts:
        accounts[user_id] += amount
        print(f"Deposited {amount} into account of user {user_id}")
        check_balance(user_id)
    else:
        print("Account does not exist.")

def withdraw(user_id, amount):
    if user_id in accounts:
        if accounts[user_id] >= amount:
            accounts[user_id] -= amount
            print(f"Withdrew {amount} from account of user {user_id}")
            check_balance(user_id)
        else:
            print("Insufficient balance.")
    else:
        print("Account does not exist.")

def delete_account(user_id):
    if user_id in accounts:
        del accounts[user_id]
        print(f"Account of user {user_id} deleted.")
    else:
        print("Account does not exist.")

# Interactive loop
while True:
    print("\nWelcome to Simple Banking System")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Delete Account")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user_id = input("Enter user ID: ")
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
