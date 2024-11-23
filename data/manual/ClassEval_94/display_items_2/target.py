class VendingMachine:
    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, list.
        """
        if len(self.inventory) == 0:
            return False
        else:
            product_list = []
            for product, details in self.inventory.items():
                price = details['price']
                quantity = details['quantity']
                product_info = f"{product} - ${price} [{quantity}]"
                product_list.append(product_info)
            return product_list