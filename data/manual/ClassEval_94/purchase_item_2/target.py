class VendingMachine:
    def purchase_item(self, item_name):
        """
        Purchases a product from the vending machine and returns the balance after the purchase and display purchase unsuccessful if the product is out of stock.
        :param item_name: The name of the product to be purchased, str.
        :return: If successful, returns the balance of the vending machine after the product is purchased, float,otherwise,returns False.
        """
        if item_name in self.inventory and self.inventory[item_name]['quantity'] > 0:
            self.inventory[item_name]['quantity'] -= 1
            self.balance -= self.inventory[item_name]['price']
            print("Purchase successful!")
            return self.balance
        else:
            print("Purchase unsuccessful. Product is out of stock.")
            return False