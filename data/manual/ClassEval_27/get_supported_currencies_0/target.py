class CurrencyConverter:
    def get_supported_currencies(self):
        """
        Returns a list of supported currency types
        :return: list, All supported currency types
        """
        return list(self.rates.keys())