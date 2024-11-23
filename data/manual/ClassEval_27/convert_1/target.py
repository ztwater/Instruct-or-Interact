class CurrencyConverter:
    def convert(self, amount, from_currency, to_currency):
        """
        Convert the value of a given currency to another currency type
        :param amount: float, The value of a given currency
        :param from_currency: string, source currency type
        :param to_currency: string, target currency type
        :return: float, value converted to another currency type
        """
        conversion_rates = {
            'USD': {
                'EUR': 0.85,
                'GBP': 0.72,
                'JPY': 110.15,
                'CAD': 1.23,
                'AUD': 1.34,
                'CNY': 6.40,
            },
            'EUR': {
                'USD': 1.18,
                'GBP': 0.86,
                'JPY': 130.12,
                'CAD': 1.45,
                'AUD': 1.58,
                'CNY': 7.54,
            },
            'GBP': {
                'USD': 1.37,
                'EUR': 1.16,
                'JPY': 151.32,
                'CAD': 1.70,
                'AUD': 1.85,
                'CNY': 8.80,
            },
            'JPY': {
                'USD': 0.0091,
                'EUR': 0.0077,
                'GBP': 0.0066,
                'CAD': 0.0093,
                'AUD': 0.0101,
                'CNY': 0.061,
            },
            'CAD': {
                'USD': 0.81,
                'EUR': 0.69,
                'GBP': 0.59,
                'JPY': 107.42,
                'AUD': 1.09,
                'CNY': 5.27,
            },
            'AUD': {
                'USD': 0.75,
                'EUR': 0.63,
                'GBP': 0.54,
                'JPY': 94.54,
                'CAD': 0.92,
                'CNY': 4.49,
            },
            'CNY': {
                'USD': 0.16,
                'EUR': 0.13,
                'GBP': 0.11,
                'JPY': 16.42,
                'CAD': 0.19,
                'AUD': 0.22,
            },
        }
    
        if from_currency not in conversion_rates or to_currency not in conversion_rates:
            return "Invalid currency type"