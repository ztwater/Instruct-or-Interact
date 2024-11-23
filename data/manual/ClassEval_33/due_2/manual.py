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
        """
        amount = self.total()  # Calculate the total amount of the order
        discount = 0
        
        if self.promotion is not None:  # Check if a promotion function is provided
            discount = self.promotion(self.cart)  # Apply the promotion function to calculate the discount
        
        final_amount = amount - (amount * discount)  # Calculate the final amount to be paid
        
        return final_amount

### Adaptation:
Total number: 14
### Raw Output:
Here is the adapted method `due()` in the context of the `DiscountStrategy` class:

```
    def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        """
        amount = self.total()  # Calculate the total amount of the order
        discount = 0
        
        if self.promotion is not None:  # Check if a promotion function is provided
            discount = self.promotion(self.cart)  # Apply the promotion function to calculate the discount
        
        final_amount = amount - (amount * discount)  # Calculate the final amount to be paid
        
        return final_amount
```

This adapted `due()` method takes into account the `total()` method to calculate the total amount of the order. It checks if a promotion function is provided and applies it to calculate the discount. Finally, it calculates the final amount to be paid by subtracting the discount from the total amount. The final amount is then returned as a float value.

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
# 4 errors, 0 failures in 5 runs.
# errors:
#     AttributeError:
#         test_due_2: 'list' object has no attribute 'customer'
#         test_due_3: 'list' object has no attribute 'cart'
#         test_due_4: 'list' object has no attribute 'cart'
#         test_due_5: 'list' object has no attribute 'customer'
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.promotion
# method_dependencies: total


