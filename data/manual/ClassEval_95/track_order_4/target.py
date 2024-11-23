class Warehouse:
    def track_order(self, order_id):
        """
        Get the status of specific order.
        :param order_id: int
        :return False: only if the order_id is not in self.orders.
        """
        import sqlite3
        
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT status FROM orders WHERE order_id = ?", (order_id,))
        
        result = cursor.fetchone()
        
        conn.close()
        
        if result is not None:
            return result[0]
        else:
            return "Order not found"