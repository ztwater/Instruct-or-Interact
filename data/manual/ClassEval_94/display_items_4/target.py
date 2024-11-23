class VendingMachine:
    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, list.
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.display_items()
        False
        >>> vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10} }
        >>> vendingMachine.display_items()
        'Coke - $1.25 [10]'

        """
        if len(self.inventory) == 0:
            return False
        else:
            for item in self.inventory:
                price = self.inventory[item]['price']
                quantity = self.inventory[item]['quantity']
                print(f"{item} - ${price} [{quantity}]")