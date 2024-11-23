class Warehouse:
    def change_order_status(self, order_id, new_status):
        for order in self.orders:
            if order['order_id'] == order_id:
                order['status'] = new_status
                break