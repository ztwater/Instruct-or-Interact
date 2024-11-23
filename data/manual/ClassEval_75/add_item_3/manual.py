### Method Description:
    def add_item(self, item, price, quantity=1):
        """
        Add item information to the shopping list items, including price and quantity. The default quantity is 1
        :param item: string, Item to be added
        :param price: float, The price of the item
        :param quantity:int, The number of items, defaults to 1
        :return:None
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        self.items = {"apple":{"price":1, "quantity":5}}
        """

### Solution Code:
    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item] = {'price': price, 'quantity': quantity}
        else:
            self.items[item] = {'price': price, 'quantity': quantity}

### Source Code:
    def add_item(item_name, price, quantity=1):
        shopping_list[item_name] = {'price': price, 'quantity': quantity}

### Predicted Code:
    def add_item(self, item, price, quantity=1):
        """
        Add item information to the shopping list items, including price and quantity. The default quantity is 1
        :param item: string, Item to be added
        :param price: float, The price of the item
        :param quantity:int, The number of items, defaults to 1
        :return:None
        """
        self.items[item] = {"price": price, "quantity": quantity}

### Adaptation:
Total number: 8
### Raw Output:
```
def add_item(self, item, price, quantity=1):
    """
    Add item information to the shopping list items, including price and quantity. The default quantity is 1
    :param item: string, Item to be added
    :param price: float, The price of the item
    :param quantity:int, The number of items, defaults to 1
    :return:None
    """
    self.items[item] = {"price": price, "quantity": quantity}
```

### Test Code:
class ShoppingCartTestAddItem(unittest.TestCase):
    def test_add_item_1(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        self.assertEqual(shoppingcart.items, {"apple": {"price": 1, "quantity": 5}})

    def test_add_item_2(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1)
        self.assertEqual(shoppingcart.items, {"apple": {"price": 1, "quantity": 1}})

    def test_add_item_3(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("aaa", 1)
        self.assertEqual(shoppingcart.items, {"aaa": {"price": 1, "quantity": 1}})

    def test_add_item_4(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("bbb", 1)
        self.assertEqual(shoppingcart.items, {"bbb": {"price": 1, "quantity": 1}})

    def test_add_item_5(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("ccc", 1)
        self.assertEqual(shoppingcart.items, {"ccc": {"price": 1, "quantity": 1}})

    def test_add_item_6(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        shoppingcart.add_item("apple", 1, 5)
        self.assertEqual(shoppingcart.items, {"apple": {"price": 1, "quantity": 5}})

### Test Output:
# 0 errors, 0 failures in 6 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.items
# method_dependencies: 


