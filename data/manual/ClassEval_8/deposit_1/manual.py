### Method Description:
    def deposit(self, amount):
        """
        Deposits a certain amount into the account, increasing the account balance, return the current account balance.
        If amount is negative, raise a ValueError("Invalid amount").
        :param amount: int
        """

### Solution Code:
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Invalid amount")
        self.balance += amount
        return self.balance

### Source Code:
    def deposit(amount, account_balance):
        account_balance += amount
        return account_balance

### Predicted Code:
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Invalid amount")
        self.balance += amount
        return self.balance

### Adaptation:
Total number: 11
### Raw Output:
```python
def deposit(self, amount):
    if amount < 0:
        raise ValueError("Invalid amount")
    self.balance += amount
    return self.balance
```

### Test Code:
class BankAccountTestDeposit(unittest.TestCase):

    def test_deposit(self):
        account1 = BankAccount()
        ret = account1.deposit(1000)
        self.assertEqual(ret, 1000)

    def test_deposit_2(self):
        account1 = BankAccount()
        account1.deposit(1000)
        ret = account1.deposit(2000)
        self.assertEqual(ret, 3000)


    def test_deposit_3(self):
        account1 = BankAccount()
        with self.assertRaises(ValueError) as context:
            account1.deposit(-1000)
        self.assertEqual(str(context.exception), "Invalid amount")

    def test_deposit_4(self):
        account1 = BankAccount()
        ret = account1.deposit(0)
        self.assertEqual(ret, 0)

    def test_deposit_5(self):
        account1 = BankAccount()
        account1.deposit(1000)
        ret = account1.deposit(1000)
        self.assertEqual(ret, 2000)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.balance
# method_dependencies: 


