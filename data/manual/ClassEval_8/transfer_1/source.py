class BankAccount:
    def transfer(amount, current_account, other_account):
        if amount <= current_account.balance:
            current_account.balance -= amount
            other_account.balance += amount
            return True
        else:
            return False