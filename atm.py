import random
import getpass
import string

class Account:
    # Construct an Account object
    def __init__(self, pin, balance = 0):
        self.pin = pin
        self.balance = balance

    def getPin(self):
        return self.pin

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount



def main():
   # Creating accounts
   accounts = []
   for i in range(1000, 9999):
       account = Account(i, 0)
       accounts.append(account)

# ATM Processes
   while True:

       # Reading pin from user
       pin = int(getpass.getpass(' ENTER PIN: '))

       # Loop till pin is valpin
       while pin < 1000 or pin > 9999:
           pin = int(getpass.getpass('WRONG ENTER PIN: '))

       # Iterating over account session
       while True:

           # Printing menu
           print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")

           # Reading selection
           selection = int(input("\nEnter your selection: "))

           # Getting account object
           for acc in accounts:
               # Comparing account pin
               if acc.getPin() == pin:
                   accountObj = acc
                   break

           # View Balance
           if selection == 1:
               # Printing balance
               print(accountObj.getBalance())

           # Withdraw
           elif selection == 2:
               # Reading amount
               amt = float(input("\nEnter amount to withdraw: "))
               ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")

               if ver_withdraw == "Yes":
                   print("Verify withdraw")
               else:
                   break

               if amt < accountObj.getBalance():
                  # Calling withdraw method
                  accountObj.withdraw(amt)
                  # Printing updated balance
                  print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
               else:
                    print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()) + " n")
                    print("\nPlease make a deposit.");

           # Deposit
           elif selection == 3:
               # Reading amount
               amt = float(input("\nEnter amount to deposit: "))
               ver_deposit = input("Is this the correct amount, Yes, or No ? " + str(amt) + " ")

               if ver_deposit == "Yes":
                  # Calling deposit method
                  accountObj.deposit(amt);
                  # Printing updated balance
                  print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
               else:
                   break

           elif selection == 4:
               print("*********************************")
               print("Transaction is now complete.")
               print("*********************************")
               print("Transaction number: ", random.randint(10000, 1000000))
               print("********************************")
               print("Thanks for choosing us as your bank")
               print("********************************")
               exit()

           # Any other choice
           else:
               print("\nThat's an invalpin choice.")

# Main function
main()
