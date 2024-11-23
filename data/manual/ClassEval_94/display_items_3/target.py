class VendingMachine:
    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, list.
        """
        if not self.inventory:
            return False
        else:
            displayed_items = []
            for item_name, item_info in self.inventory.items():
                price = item_info['price']
                quantity = item_info['quantity']
                item_string = f"{item_name} - ${price} [{quantity}]"
                displayed_items.append(item_string)
            return displayed_items