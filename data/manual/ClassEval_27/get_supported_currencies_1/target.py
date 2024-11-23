class CurrencyConverter:
    def get_supported_currencies(self):
        """
        Returns a list of supported currency types
        :return:list, All supported currency types
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies()
        ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
        """
        supported_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY']
        return supported_currencies