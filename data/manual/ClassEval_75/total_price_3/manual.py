### Method Description:
    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price
        :return:float, the total price of all items in the shopping list
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.add_item("banana", 2, 3)
        >>> shoppingcart.total_price()
        11.0
        """

### Solution Code:
    def total_price(self) -> float:
        return sum([item['quantity'] * item['price'] for item in self.items.values()])

### Source Code:
    def total_price(shopping_list):
        total = 0
        for item in shopping_list:
            quantity = item['quantity']
            price = item['price']
            total += quantity * price
        return total

### Predicted Code:
    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price
        :return:float, the total price of all items in the shopping list
        """
        total = 0
        for item, details in self.items.items():
            quantity = details['quantity']
            price = details['price']
            total += quantity * price
        return total

### Adaptation:
Total number: 14
### Raw Output:
```python
    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price
        :return:float, the total price of all items in the shopping list
        """
        total = 0
        for item, details in self.items.items():
            quantity = details['quantity']
            price = details['price']
            total += quantity * price
        return total
```

### Test Code:
class ShoppingCartTestTotalPrice(unittest.TestCase):
    def test_total_price_1(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        shoppingcart.add_item("banana", 2, 3)
        self.assertEqual(shoppingcart.total_price(), 11.0)

    def test_total_price_2(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        shoppingcart.add_item("banana", 2, 3)
        shoppingcart.remove_item("apple", 3)
        self.assertEqual(shoppingcart.total_price(), 8.0)

    def test_total_price_3(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 1)
        shoppingcart.add_item("banana", 2, 1)
        self.assertEqual(shoppingcart.total_price(), 3.0)

    def test_total_price_4(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 2)
        shoppingcart.add_item("banana", 2, 1)
        self.assertEqual(shoppingcart.total_price(), 4.0)

    def test_total_price_5(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 3)
        shoppingcart.add_item("banana", 2, 1)
        self.assertEqual(shoppingcart.total_price(), 5.0)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.items
# method_dependencies: 


