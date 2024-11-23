class Warehouse:
    def change_order_status(self, order_id, status):
        """
        Change the status of order if the input order_id is in self.orders.
        :param order_id: int
        :param status: str, the state that is going to change to
        :return False: only if the order_id is not in self.orders
        """
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
        else:
            return False