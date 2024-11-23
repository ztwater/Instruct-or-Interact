class Warehouse:
    def update_product_quantity(self, product_id, quantity):
        for product_id, product in self.inventory.items():
            if product_id == product_id:
                product['quantity'] += quantity
                break
        else:
            self.inventory[product_id] = {'name': product['name'], 'quantity': quantity}