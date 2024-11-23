class VendingMachine:
    def purchase_item(self, item_name):
        if item_name in self.inventory:
            if self.inventory[item_name]['quantity'] > 0:
                self.inventory[item_name]['quantity'] -= 1
                self.balance -= self.inventory[item_name]['price']
                return self.balance
            else:
                print("Purchase unsuccessful. Product is out of stock.")
                return False
        else:
            print("Purchase unsuccessful. Product not found.")
            return False