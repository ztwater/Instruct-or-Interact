class Warehouse:
    def add_product(inventory, product, quantity):
        if product in inventory:
            inventory[product] += quantity
        else:
            inventory[product] = quantity
        return inventory