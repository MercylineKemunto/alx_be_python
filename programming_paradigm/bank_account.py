class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional intial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        """Deduct the amount from the acount balance if funds are sufficient."""
        if amount > self.account_balance:
            return False #Insufficient funds
        elif amount > 0:
            self.account_balance -= amount
            return True
        else:
            print("Withdrawal amount must be positive.")
            return False
    def display_balance(self):
            """Print the account balance."""
            print(f"Current Balance: ${self.account_balance:.2f}")

