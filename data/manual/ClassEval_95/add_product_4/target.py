class Warehouse:
    def add_product(self, product_id, name, quantity):
        if product_id in self.inventory:
            self.inventory[product_id]["quantity"] += quantity
        else:
            self.inventory[product_id] = {"name": name, "quantity": quantity}