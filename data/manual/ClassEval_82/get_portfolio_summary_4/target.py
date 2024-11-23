class StockPortfolioTracker:
    def get_portfolio_summary(self):
        total_value = self.calculate_portfolio_value()
        summary = []
        for stock in self.portfolio:
            stock_value = self.get_stock_value(stock)
            percentage = (stock_value / total_value) * 100
            summary.append({'name': stock['name'], 'value': stock_value})
        
        return total_value, summary