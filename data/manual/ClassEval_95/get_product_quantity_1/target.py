class Warehouse:
    def get_product_quantity(self, product_id):
        """
        Get the quantity of specific product by product_id.
        :param product_id, int
        :return: if the product_id is in inventory then return the corresponding quantity,
                 or False otherwise.
        """
        if product_id in self.inventory:
            return self.inventory[product_id].quantity
        else:
            return False
