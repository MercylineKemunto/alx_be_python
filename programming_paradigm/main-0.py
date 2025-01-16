import sys
from bank_account import BankAccount
def main():
    #Create a BankAccount instance with an initial balance of $100
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    try:
        command_parts = sys.argv[1].split(':')
        command = command_parts[0].lower()
        amount = float(command_parts[1]) if len(command_parts) > 1 else None
    except (IndexError, ValueError):
            print("Invalid input format. Use <command>:<amount> for deposit or withdraw.")
            sys.exit(1)

        
    if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
    elif command == "Withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insuffient funds.")
    elif command == "display":
            account.display_balance()
    else:
            print("Invalid command. Use deposit, withdraw, or display.")
    
if __name__ == "__main__":
    main() 
