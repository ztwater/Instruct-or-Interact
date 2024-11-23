class StockPortfolioTracker:
    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        """
        total_value = 0
        for stock in self.portfolio:
            total_value += stock['quantity'] * stock['price']
        
        summary = []
        for stock in self.portfolio:
            stock_value = stock['quantity'] * stock['price']
            stock_summary = {'name': stock['name'], 'value': stock_value}
            summary.append(stock_summary)
        
        return (total_value, summary)