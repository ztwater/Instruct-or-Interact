class StockPortfolioTracker:
    def remove_stock(portfolio, stock):
        if stock in portfolio:
            del portfolio[stock]
            print(f"{stock} has been removed from the portfolio.")
        else:
            print(f"{stock} is not in the portfolio.")
    