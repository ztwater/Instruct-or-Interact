class Warehouse:
    def change_order_status(self, order_id, status):
        if order_id not in self.orders:
            return False
        self.orders[order_id]['status'] = status