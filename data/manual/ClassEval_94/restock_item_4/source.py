class VendingMachine:
    def restock_item(product, quantity):
        # Check if the product is already in the vending machine
        if product in vending_machine:
            # Add the quantity to the existing inventory
            vending_machine[product] += quantity
        else:
            # If the product is not in the vending machine, add it with the specified quantity
            vending_machine[product] = quantity