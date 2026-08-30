pin = "1234"
balance = 10000
attempts = 0
while attempts < 5:
    entered_pin = input("Enter ATM PIN: ")
    if entered_pin == pin:
        print("\nLogin Successful!")
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                print(f"Your Balance: Rs.{balance}")

            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                balance += amount
                print(f"Rs.{amount} deposited successfully.")
                print(f"New Balance: Rs.{balance}")

            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))

                if amount <= balance:
                    balance -= amount
                    print(f"Rs.{amount} withdrawn successfully.")
                    print(f"Remaining Balance: Rs.{balance}")
                else:
                    print("Insufficient Balance!")

            elif choice == "4":
                print("Thank you for using our ATM.")
                break

            else:
                print("Invalid Option!")

        break

    else:
        attempts += 1
        remaining = 5 - attempts
        print(f"Incorrect PIN! Remaining Attempts: {remaining}")

if attempts == 5:
    print("\nATM Blocked! Too many incorrect attempts.")
