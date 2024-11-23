class StockPortfolioTracker:
    def calculate_portfolio_value(self):
        total_value = 0
            
        for stock in self.portfolio:
            stock_value = stock['price'] * stock['quantity']
            total_value += stock_value
            
        return total_value