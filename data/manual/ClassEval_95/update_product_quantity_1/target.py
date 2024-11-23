class Warehouse:
    def update_product_quantity(self, product_id, quantity):
        for product_id, product_details in self.inventory.items():
            if product_id == product_id:
                product_details['quantity'] += quantity
                break
        else:
            # If product_id is not found in inventory, create a new product entry
            self.inventory[product_id] = {'name': product_details['name'], 'quantity': quantity}