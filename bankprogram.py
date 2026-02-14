def showbalance(balance):
    print(f"Your current balance is: ${balance:.2f}")
def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
        return amount
    else:
        print("Invalid amount. Deposit must be greater than zero.")
        return 0
def withdraw():
    amount = float(input("Enter the amount to withdraw: "))
    if amount > 0:
        return -amount
    else:
        print("Invalid amount. Withdrawal must be greater than zero.")
        return 0
balance = 0
isrunning = True
while isrunning:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        showbalance(balance)
    elif choice == '2':
        balance = deposit()
    elif choice == '3':
        balance = withdraw()
    elif choice == '4':
        isrunning = False
    else:
        print("Invalid choice. Please try again.")
print("Thank you for using the banking program. Goodbye!")