class CurrencyConverter:
    def add_currency_rate(self, currency, rate):
        """
        Add a new supported currency type, return False if the currency type is already in the support list
        :param currency: string, currency type to be added
        :param rate: float, exchange rate for this type of currency
        :return: If successful, returns None; if unsuccessful, returns False
        >>> cc = CurrencyConverter()
        >>> cc.add_currency_rate('KRW', 1308.84)
        self.rates['KRW'] = 1308.84
        """
        if currency in self.rates:
            return False
        else:
            self.rates[currency] = rate
            return None