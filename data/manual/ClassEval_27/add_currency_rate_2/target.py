class CurrencyConverter:
    def add_currency_rate(self, currency, rate):
        if currency in self.rates:
            return False
        else:
            self.rates[currency] = rate
            return None