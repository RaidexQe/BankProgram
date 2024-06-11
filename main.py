
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")
    pass


def deposit():
    amount = float(input("Enter the amount to be deposited: "))
    
    if amount < 0: 
        print("That's not the valid anount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount= float(input("Enter the amount to be withdrawed "))
    
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
    

def main():
    try:
        with open("balance.txt", "r") as file:
            balance = float(file.read())
    except FileNotFoundError:
        balance = 0
        
    is_running = True

    while is_running:
        print("*" * 100)
        print("      🏦Banking Program🏦   ")
        print("1.💵Show balance💵")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*" * 100)
        
        choice = input("Enter your choice from (1-4): ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Invalid choice")
            
    with open("balance.txt", "w") as file:
        file.write(str(balance))


    print("Thank you for banking with us😁😁")
    
    
if __name__ == "__main__":   
    main()
            
