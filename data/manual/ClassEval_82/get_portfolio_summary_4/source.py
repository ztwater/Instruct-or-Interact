class StockPortfolioTracker:
    def get_portfolio_summary(portfolio):
        total_value = 0
        for stock in portfolio:
            total_value += stock['quantity'] * stock['price']
        
        summary = f"Portfolio Summary:\nTotal Value: ${total_value}\n"
        for stock in portfolio:
            stock_value = stock['quantity'] * stock['price']
            percentage = (stock_value / total_value) * 100
            summary += f"{stock['symbol']}: ${stock_value} ({percentage:.2f}%)\n"
        
        return summary