class StockPortfolioTracker:
    def sell_stock(self, stock):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        """
        if stock in self.portfolio:
            self.cash_balance += stock['price'] * stock['quantity']
            self.portfolio.remove(stock)
            return True
        else:
            return False