
class BankAccount:
    """A simple BankAccount class using OOP principles."""

    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw amount if funds are available.
        Returns True on success, False if insufficient balance.
        """
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    def display_balance(self):
        """Print the current account balance formatted to two decimals."""
        print(f"Current Balance: ${self.account_balance:.2f}")

    

    
