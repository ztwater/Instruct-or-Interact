class CurrencyConverter:
    def add_currency_rate(currency_type, supported_currencies):
        if currency_type in supported_currencies:
            return False
        else:
            supported_currencies.append(currency_type)
            return True