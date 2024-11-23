class StockPortfolioTracker:
    def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: the value of the stock, float.
        """
        stock_value = stock['price'] * stock['quantity']
        return stock_value