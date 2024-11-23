class VendingMachine:
    def add_item(product, quantity, inventory):
        if product in inventory:
            inventory[product] += quantity
        else:
            inventory[product] = quantity