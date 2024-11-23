class StockPortfolioTracker:
    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.calculate_portfolio_value()
        11500.0
        """
        total_value = 0
        
        for stock in self.portfolio:
            stock_value = stock['price'] * stock['quantity']
            total_value += stock_value
        
        return total_value