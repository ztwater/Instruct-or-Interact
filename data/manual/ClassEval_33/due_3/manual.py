### Method Description:
    def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> ds = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> ds.due()
        312.55

        """

### Solution Code:
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.__total - discount

### Source Code:
    def due(amount, discount):
        final_amount = amount - (amount * discount)
        return final_amount

### Predicted Code:
    def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> ds = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> ds.due()
        312.55
        """
        amount = self.total()
        discount = self.promotion(self)
        final_amount = amount - (amount * discount)
        return final_amount

### Adaptation:
Total number: 11
### Raw Output:
Here is the adapted method `due` for the `DiscountStrategy` class:

```python
def due(self):
    """
    Calculate the final amount to be paid after applying the discount.
    :return: float, final amount to be paid
    >>> customer = {'name': 'John Doe', 'fidelity': 1200}
    >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
    >>> ds = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
    >>> ds.due()
    312.55
    """
    amount = self.total()
    discount = self.promotion(self)
    final_amount = amount - (amount * discount)
    return final_amount
```

This adapted method calculates the final amount to be paid after applying the discount. It calls the `total` method to calculate the initial amount, and then calls the `promotion` function (based on the provided promotion) to get the discount. Finally, it calculates the final amount by subtracting the discount from the initial amount and returns the result.

### Test Code:
class DiscountStrategyTestDue(unittest.TestCase):
    def test_due_1(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart)
        expected_due = 250.0
        actual_due = order.due()
        self.assertEqual(actual_due, expected_due)

    def test_due_2(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        expected_due = 237.5
        actual_due = order.due()
        self.assertEqual(actual_due, expected_due)

    def test_due_3(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 20, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
        expected_due = 410.0
        actual_due = order.due()
        self.assertEqual(actual_due, expected_due)

    def test_due_4(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': f'product{i}', 'quantity': 1, 'price': 10.0} for i in range(15)]
        order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
        expected_due = 139.5
        actual_due = order.due()
        self.assertEqual(actual_due, expected_due)

    def test_due_5(self):
        customer = {'name': 'John Doe', 'fidelity': 900}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        expected_due = 250.0
        actual_due = order.due()
        self.assertEqual(actual_due, expected_due)

### Test Output:
# 1 errors, 3 failures in 5 runs.
# errors:
#     TypeError:
#         test_due_1: 'NoneType' object is not callable
# failures:
#     AssertionError:
#         test_due_2: -2875.0 != 237.5
#         test_due_3: -17550.0 != 410.0
#         test_due_4: -1425.0000000000002 != 139.5


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.promotion
# method_dependencies: total


