class CurrencyConverter:
    def update_currency_rate(self, currency, new_rate):
        """
        Update the exchange rate for a certain currency
        :param currency:string
        :param new_rate:float
        :return:If successful, returns None; if unsuccessful, returns False
        """
        if currency in self.rates:
            self.rates[currency] = new_rate
            return None
        else:
            return False
