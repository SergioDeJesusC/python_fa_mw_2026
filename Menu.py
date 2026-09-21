balance = 1000.00
choice = 1
while choice > 0 and choice < 4:
    print(f" 1. Balance")
    print(f" 2. Deposit")
    print(f" 3. Withdraw")
    print(f" 4. Exit")
    choice = int(input("Please enter the number of your selection:  "))
    
    match choice:
        case 1:
            print("Balance")
            print(f"Your balance is:  ${balance:.2f}")
        case 2:
            print("Deposit")
            print(f"How much you wnat to deposit")
        case 3:
            print("Withdraw")
            print(f"How much you want to Withdraw")
        case 4:
            print("Good bye!")
