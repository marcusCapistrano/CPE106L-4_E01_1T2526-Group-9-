from bank import SavingsAccount, Bank
from bank_sort import printAccountsByBalance

if __name__ == "__main__":
    bank = Bank()

    # Create accounts
    a1 = SavingsAccount("Neo", "1234", 1500)
    a2 = SavingsAccount("Marcus", "5678", 500)
    a3 = SavingsAccount("Kyle", "9999", 3000)

    # Add to bank
    bank.add(a1)
    bank.add(a2)
    bank.add(a3)

    # Print all accounts
    print("All Accounts:")
    print(bank)

    # Print total assets
    print("\nTotal Assets:", bank.getTotalAssets())

    # Print accounts sorted by balance
    print("\nAccounts in order by balance:")
    printAccountsByBalance(bank)
