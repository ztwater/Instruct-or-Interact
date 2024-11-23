class VendingMachine:
    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, list.
        """
        if not self.inventory:
            return False
        else:
            products_list = []
            for product, details in self.inventory.items():
                item_name = product
                price = details['price']
                quantity = details['quantity']
                product_info = f"{item_name} - ${price} [{quantity}]"
                products_list.append(product_info)
            return products_list