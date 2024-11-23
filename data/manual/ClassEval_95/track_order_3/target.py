class Warehouse:
    def track_order(self, order_id):
        """
        Get the status of specific order.
        :param order_id: int
        :return False: only if the order_id is not in self.orders.
        """
        # Check if the order exists in self.orders
        if order_id in self.orders:
            # Get the order's status
            status = self.orders[order_id].status
            return status
        else:
            return False