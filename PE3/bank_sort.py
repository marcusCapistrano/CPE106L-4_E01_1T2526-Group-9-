from bank import SavingsAccount, Bank

def printAccountsByBalance(bank, descending=False):
    """Print accounts sorted by balance (ascending by default)."""
    accounts_sorted = sorted(bank._accounts, key=lambda a: a.getBalance(), reverse=descending)
    for acct in accounts_sorted:
        print(acct)

# demo
if __name__ == "__main__":
    bank = Bank()
    bank.add(SavingsAccount("Neo", "1234", 1000))
    bank.add(SavingsAccount("Alex", "5678", 500))
    bank.add(SavingsAccount("Lara", "9999", 2000))

    print("Accounts sorted by balance:")
    printAccountsByBalance(bank)