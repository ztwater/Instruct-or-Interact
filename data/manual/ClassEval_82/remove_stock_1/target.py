class StockPortfolioTracker:
    def remove_stock(self, stock):
        if stock in self.portfolio:
            self.portfolio.remove(stock)
            print(f"{stock} has been removed from the portfolio.")
            return True
        else:
            print(f"{stock} is not in the portfolio.")
            return False