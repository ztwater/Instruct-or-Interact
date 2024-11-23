class StockPortfolioTracker:
    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        stock_price = stock["price"]
        stock_quantity = stock["quantity"]
        total_cost = stock_price * stock_quantity
        
        if self.cash_balance >= total_cost:
            self.cash_balance -= total_cost
            self.portfolio.append(stock)
            return True
        else:
            return False