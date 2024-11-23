### Method Description:
    def update_product_quantity(self, product_id, quantity):
        """
        According to product_id, add the quantity to the corresponding product in inventory.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.update_product_quantity(1, -1)
        >>> warehouse.inventory
        {1: {'name': 'product1', 'quantity': 2}}
        """

### Solution Code:
    def update_product_quantity(self, product_id, quantity):
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity

### Source Code:
    def update_product_quantity(inventory, product_id, quantity):
        for product in inventory:
            if product['product_id'] == product_id:
                product['quantity'] += quantity
                break
        else:
            # If product_id is not found in inventory, create a new product entry
            inventory.append({'product_id': product_id, 'quantity': quantity})

### Predicted Code:
    def update_product_quantity(self, product_id, quantity):
        for product in self.inventory.values():
            if product['product_id'] == product_id:
                product['quantity'] += quantity
                break
        else:
            # If product_id is not found in inventory, create a new product entry
            self.inventory[product_id] = {'product_id': product_id, 'quantity': quantity}

### Adaptation:
Total number: 14
### Raw Output:
```
    def update_product_quantity(self, product_id, quantity):
        for product in self.inventory.values():
            if product['product_id'] == product_id:
                product['quantity'] += quantity
                break
        else:
            # If product_id is not found in inventory, create a new product entry
            self.inventory[product_id] = {'product_id': product_id, 'quantity': quantity}
```

### Test Code:
class WarehouseTestUpdateProductQuantity(unittest.TestCase):
    def test_update_product_quantity_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.update_product_quantity(1, 5)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product 1', 'quantity': 15}})

    # quantity is negative
    def test_update_product_quantity_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.update_product_quantity(1, -5)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product 1', 'quantity': 5}})

    def test_update_product_quantity_3(self):
        warehouse = Warehouse()
        warehouse.update_product_quantity(1, -5)
        self.assertEqual(warehouse.inventory, {})

    def test_update_product_quantity_4(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.update_product_quantity(1, 1)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product 1', 'quantity': 11}})

    def test_update_product_quantity_5(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.update_product_quantity(1, -9)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product 1', 'quantity': 1}})

### Test Output:
# 4 errors, 1 failures in 5 runs.
# errors:
#     KeyError:
#         test_update_product_quantity_1: 'product_id'
#         test_update_product_quantity_2: 'product_id'
#         test_update_product_quantity_4: 'product_id'
#         test_update_product_quantity_5: 'product_id'
# failures:
#     AssertionError:
#         test_update_product_quantity_3: {1: {'product_id': 1, 'quantity': -5}} != {}


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.inventory
# method_dependencies: 


