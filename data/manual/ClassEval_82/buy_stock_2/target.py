class StockPortfolioTracker:
    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        if self.cash_balance < stock['price'] * stock['quantity']:
            return False
        else:
            self.cash_balance -= stock['price'] * stock['quantity']
            self.portfolio.append(stock)
            return True