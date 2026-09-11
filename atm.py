class ATM:
    def __init__(self, balance):
        self.balance = balance
        self.pin = "1234"
        self.attempts = 5
    def login(self):
        while self.attempts > 0:
            entered_pin = input("Enter PIN: ")

            if entered_pin == self.pin:
                print("Login Successful!")
                self.menu()
                return
            self.attempts -= 1
            print("Wrong PIN")
            print("Attempts Left:", self.attempts)

        print("Account Blocked!")

    def menu(self):
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Choose Option: ")

            if choice == "1":
                print("Current Balance:", self.balance)

            elif choice == "2":
                amount = float(input("Enter Deposit Amount: "))
                self.balance += amount
                print("Amount Deposited Successfully")

            elif choice == "3":
                amount = float(input("Enter Withdraw Amount: "))

                if amount <= self.balance:
                    self.balance -= amount
                    print("Withdrawal Successful")
                else:
                    print("Insufficient Balance")

            elif choice == "4":
                print("Thank You For Using ATM")
                break

            else:
                print("Invalid Option")


user1 = ATM(10000)
user1.login()
