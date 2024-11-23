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

### Adaptation:
Total number: 34
### Raw Output:
```
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
# 0 errors, 5 failures in 5 runs.
# errors:
# failures:
#     AssertionError:
#         test_get_portfolio_summary: Tuples differ: (1500.0, [{'name': 'AAPL', 'value': 1500.0}]) != (11500.0, [{'name': 'AAPL', 'value': 1500.0}])
#         test_get_portfolio_summary_2: Tuples differ: (3000.0, [{'name': 'AAPL', 'value': 1500.0[33 chars].0}]) != (13000.0, [{'name': 'AAPL', 'value': 1500.[34 chars].0}])
#         test_get_portfolio_summary_3: Tuples differ: (0, []) != (10000.0, [])
#         test_get_portfolio_summary_4: Tuples differ: (0.0, [{'name': 'AAPL', 'value': 0.0}]) != (10000.0, [{'name': 'AAPL', 'value': 0.0}])
#         test_get_portfolio_summary_5: Tuples differ: (0.0, [{'name': 'AAPL', 'value': 0.0}]) != (10000.0, [{'name': 'AAPL', 'value': 0.0}])


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.portfolio
# method_dependencies: calculate_portfolio_value, get_stock_value


