class Warehouse:
    def update_product_quantity(inventory, product_id, quantity):
        for product in inventory:
            if product['product_id'] == product_id:
                product['quantity'] += quantity
                break
        else:
            # If product_id is not found in inventory, create a new product entry
            inventory.append({'product_id': product_id, 'quantity': quantity})