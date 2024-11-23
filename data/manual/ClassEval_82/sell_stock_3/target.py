class StockPortfolioTracker:
    def sell_stock(self, stock):
        if stock in self.portfolio:
            self.cash_balance += stock["price"] * stock["quantity"]
            self.portfolio.remove(stock)
            return True
        else:
            return False