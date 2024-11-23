class StockPortfolioTracker:
    def calculate_portfolio_value(portfolio):
        total_value = 0
        
        for stock in portfolio:
            stock_value = stock['price'] * stock['quantity']
            total_value += stock_value
        
        return total_value