class StockPortfolioTracker:
    def get_portfolio_summary(self):
        total_value = self.calculate_portfolio_value()
        summary_list = []
        for stock in self.portfolio:
            stock_value = self.get_stock_value(stock)
            stock_summary = {'name': stock['name'], 'value': stock_value}
            summary_list.append(stock_summary)
        
        return (total_value, summary_list)