class BankAccount:
    def transfer(self, other_account, amount):
        """
        Transfers a certain amount from the current account to another account.
        :param other_account: BankAccount
        :param amount: int
        >>> account1 = BankAccount()
        >>> account2 = BankAccount()
        >>> account1.deposit(1000)
        >>> account1.transfer(account2, 300)
        account1.balance = 700
        account2.balance = 300
        """
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            return True
        else:
            return False