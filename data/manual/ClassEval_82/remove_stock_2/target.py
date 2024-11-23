class StockPortfolioTracker:
    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        """
        if stock in self.portfolio:
            self.portfolio.remove(stock)
            return True
        else:
            return False