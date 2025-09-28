class SavingsAccount:
    def __init__(self, name, pin, balance=0.0, interestRate=0.02):
        self._name = name
        self._pin = pin
        self._balance = float(balance)
        self._interestRate = float(interestRate)

    def getBalance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def computeInterest(self):
        interest = self._balance * self._interestRate
        self._balance += interest
        return interest

    def __str__(self):
        return f"Name:    {self._name}\nPIN:     {self._pin}\nBalance: {self._balance:.2f}\n"


class Bank:
    def __init__(self):
        self._accounts = []

    def add(self, account):
        self._accounts.append(account)

    def remove(self, name, pin):
        for acct in self._accounts:
            if acct._name == name and acct._pin == pin:
                self._accounts.remove(acct)
                return acct
        return None

    def get(self, name, pin):
        for acct in self._accounts:
            if acct._name == name and acct._pin == pin:
                return acct
        return None

    def getTotalAssets(self):
        """Return total assets of all accounts in the bank."""
        return sum(a.getBalance() for a in self._accounts)

    def computeInterest(self):
        total = 0.0
        for a in self._accounts:
            total += a.computeInterest()
        return total

    def __str__(self):
        return '\n'.join(map(str, self._accounts))


# simple demo
if __name__ == "__main__":
    bank = Bank()
    bank.add(SavingsAccount("Neo", "1234", 1000))
    bank.add(SavingsAccount("Alex", "5678", 500))
    print(bank)
    print("Total Assets:", f"{bank.getTotalAssets():.2f}")