class StockPortfolioTracker:
    def get_portfolio_summary(self):
        total_value = self.calculate_portfolio_value()
        summary = f"Portfolio Summary:\nTotal Value: ${total_value}\n"
        
        for stock in self.portfolio:
            stock_value = self.get_stock_value(stock)
            percentage = (stock_value / total_value) * 100
            summary += f"{stock['name']}: ${stock_value} ({percentage:.2f}%)\n"
        
        return (total_value, [{'name': stock['name'], 'value': stock_value} for stock in self.portfolio])