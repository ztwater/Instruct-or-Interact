class VendingMachine:
    def purchase_item(product, stock, balance):
        if stock > 0:
            stock -= 1
            balance -= product.price
            print("Purchase successful!")
        else:
            print("Purchase unsuccessful. Product is out of stock.")
        
        return balance