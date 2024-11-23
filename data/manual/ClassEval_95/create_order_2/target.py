class Warehouse:
    def create_order(self, order_id, product_id, quantity):
        """
        Create an order which includes the information of a product, such as its id and quantity.
        Put the new order into self.orders.
        The default value of the status is 'Shipped'.
        :param order_id: int
        :param product_id: int
        :param quantity: the quantity of the product that is selected.
        :return: False if product_id is not in inventory or the quantity is not adequate
        """
        if product_id not in self.inventory or quantity > self.inventory[product_id]['quantity']:
            return False
        
        order = {
            'product_id': product_id,
            'quantity': quantity,
            'status': 'Shipped'
        }
        
        self.orders[order_id] = order