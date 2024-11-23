class StockPortfolioTracker:
    def sell_stock(stock, portfolio, cash_balance):
        if stock in portfolio:
            cash_balance += portfolio[stock]
            del portfolio[stock]
            return cash_balance
        else:
            return cash_balance