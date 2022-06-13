# 2. Add implementation to BankAccount class methods.
# Create a subclass called SavingsAccountClass:Function Members:A constructor function to initialize the Savings account data members A
# function that will credit interest to the account A function that will debit the account for a withdrawal Data
# Members:An annual interest rate value that is credited to the account balance on a monthly basis
# class BankAccount:
#     acounte = 0
  # def __init__(self, pin):
  #   """Initial account balance is 0 and pin is 'pin'."""
  # def deposit(self, pin, amount):
  #   """Increment account balance by amount and return new balance."""
  # def withdraw(self, pin, amount):
  #   """Decrement account balance by amount and return amount withdrawn."""
  # def get_balance(self, pin):
  #   """Return account balance."""
  # def change_pin(self, oldpin, newpin):
  #   """Change pin from oldpin to newpin."""
# Add implementation to BankAccount class methods.
# Create a subclass called SavingsAccount Class:
# Function Members:
# A constructor function to initialize the Savings account data members
# A function that will credit interest to the account
# A function that will debit the account for a withdrawal
# Data Members:
# An annual interest rate value that is credited to the account balance on a monthly basis
# 3. Write a program by creating a Person and Employee classes having the following methods and print the final salary.

class BankAccount:
    """Bank Account protected by a pin number."""

    start_amount = 0

    def __init__(self, pin):
        """Initial account balance is 0 and pin is 'pin'."""

        self.pin = pin

    def deposit(self, pin, amount=0):
        """Increment account balance by amount and return new balance."""

        if pin == self.pin:
            self.start_amount += amount
        else:
            print("Pin error")

    def withdraw(self, pin, amount):
        """Decrement account balance by amount and return amount withdrawn."""
        try:
            if pin == self.pin:
                if self.start_amount - amount < 0:
                    raise ValueError
                self.start_amount -= amount
            else:
                print("Pin error")
        except ValueError:
            print("Error")

    def get_balance(self, pin):
        if pin == self.pin:
            return self.start_amount
        else:
            print("Pin error")

    def change_pin(self, oldpin, newpin):
        """Change pin from oldpin to newpin."""
        if oldpin == self.pin:
            self.pin = newpin
        else:
            print("Pin error")

    def percent_year_dep(self, amount):
        self.withdraw(4321, amount)
        amount += amount * 0.11
        self.deposit(4321, amount)

    def percent_month_dep(self, amount):
        self.withdraw(4321, amount)
        amount += amount * (0.1 / 12)
        self.deposit(4321, amount)


bank_account = BankAccount(1234)
bank_account.deposit(1234, 10000)
print(bank_account.get_balance(1234))
bank_account.change_pin(1234, 4321)
bank_account.withdraw(4321, 6500)
print(bank_account.get_balance(4321))
bank_account.deposit(4321, 10000)

bank_account.percent_year_dep(10000)
print(bank_account.get_balance(4321))
