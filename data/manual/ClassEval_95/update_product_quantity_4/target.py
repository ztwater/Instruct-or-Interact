class Warehouse:
    def update_product_quantity(self, product_id, quantity):
        for product in self.inventory.values():
            if product['product_id'] == product_id:
                product['quantity'] += quantity
                break
        else:
            # If product_id is not found in inventory, create a new product entry
            self.inventory[product_id] = {'product_id': product_id, 'quantity': quantity}