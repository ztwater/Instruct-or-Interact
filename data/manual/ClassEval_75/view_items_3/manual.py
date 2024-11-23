### Method Description:
    def view_items(self) -> dict:
        """
        Return the current shopping list items
        :return:dict, the current shopping list items
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.remove_item("apple", 3)
        >>> shoppingcart.view_items()
        {"apple":{"price":1, "quantity":2}}
        """

### Solution Code:
    def view_items(self) -> dict:
        return self.items

### Source Code:
    def view_items():
        shopping_list = ["item1", "item2", "item3"]  # replace with your actual shopping list
        return shopping_list

### Predicted Code:
    def view_items(self) -> dict:
        """
        Return the current shopping list items
        :return: dict, the current shopping list items
        """
        return self.items

### Adaptation:
Total number: 14
### Raw Output:
```python
def view_items(self) -> dict:
    """
    Return the current shopping list items
    :return: dict, the current shopping list items
    """
    return self.items
```

### Test Code:
class ShoppingCartTestViewItems(unittest.TestCase):
    def test_view_items_1(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        self.assertEqual(shoppingcart.view_items(), {"apple": {"price": 1, "quantity": 5}})

    def test_view_items_2(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 4)
        self.assertEqual(shoppingcart.view_items(), {"apple": {"price": 1, "quantity": 4}})

    def test_view_items_3(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 3)
        self.assertEqual(shoppingcart.view_items(), {"apple": {"price": 1, "quantity": 3}})

    def test_view_items_4(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 2)
        self.assertEqual(shoppingcart.view_items(), {"apple": {"price": 1, "quantity": 2}})

    def test_view_items_5(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 1)
        self.assertEqual(shoppingcart.view_items(), {"apple": {"price": 1, "quantity": 1}})

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.items
# method_dependencies: 


