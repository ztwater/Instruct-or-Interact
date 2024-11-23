### Method Description:
    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.get_portfolio_summary()
        (11500.0, [{'name': 'AAPL', 'value': 1500.0}])

        """

### Solution Code:
    def get_portfolio_summary(self):
        summary = []
        for stock in self.portfolio:
            value = self.get_stock_value(stock)
            summary.append({"name": stock["name"], "value": value})
        portfolio_value = self.calculate_portfolio_value()
        return portfolio_value, summary

### Source Code:
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

### Predicted Code:
    def get_portfolio_summary(self):
        total_value = self.calculate_portfolio_value()
        summary_list = []
        for stock in self.portfolio:
            stock_value = self.get_stock_value(stock)
            stock_summary = {'name': stock['name'], 'value': stock_value}
            summary_list.append(stock_summary)
        
        return (total_value, summary_list)

### Adaptation:
Total number: 52
### Raw Output:
```
    def get_portfolio_summary(self):
        total_value = self.calculate_portfolio_value()
        summary_list = []
        for stock in self.portfolio:
            stock_value = self.get_stock_value(stock)
            stock_summary = {'name': stock['name'], 'value': stock_value}
            summary_list.append(stock_summary)
        
        return (total_value, summary_list)
```

### Test Code:
class StockPortfolioTrackerTestGetPortfolioSummary(unittest.TestCase):
    def test_get_portfolio_summary(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        self.assertEqual(tracker.get_portfolio_summary(), (11500.0, [{'name': 'AAPL', 'value': 1500.0}]))

    def test_get_portfolio_summary_2(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10},
                             {'name': 'MSFT', 'price': 150.0, 'quantity': 10}]
        self.assertEqual(tracker.get_portfolio_summary(),
                         (13000.0, [{'name': 'AAPL', 'value': 1500.0}, {'name': 'MSFT', 'value': 1500.0}]))

    def test_get_portfolio_summary_3(self):
        tracker = StockPortfolioTracker(10000.0)
        self.assertEqual(tracker.get_portfolio_summary(), (10000.0, []))

    def test_get_portfolio_summary_4(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 0}]
        self.assertEqual(tracker.get_portfolio_summary(), (10000.0, [{'name': 'AAPL', 'value': 0.0}]))

    def test_get_portfolio_summary_5(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{'name': 'AAPL', 'price': 0.0, 'quantity': 10}]
        self.assertEqual(tracker.get_portfolio_summary(), (10000.0, [{'name': 'AAPL', 'value': 0.0}]))

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.portfolio
# method_dependencies: calculate_portfolio_value, get_stock_value


