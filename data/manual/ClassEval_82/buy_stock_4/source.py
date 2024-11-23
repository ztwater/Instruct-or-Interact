class StockPortfolioTracker:
    def buy_stock(stock, quantity, portfolio):
        if stock not in portfolio:
            portfolio[stock] = quantity
        else:
            portfolio[stock] += quantity