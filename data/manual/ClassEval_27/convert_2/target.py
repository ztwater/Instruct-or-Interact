class CurrencyConverter:
    def convert(self, amount, from_currency, to_currency):
        """
        Convert the value of a given currency to another currency type
        :param amount: float, The value of a given currency
        :param from_currency: string, source currency type
        :param to_currency: string, target currency type
        :return: float, value converted to another currency type
        """
    
        # Define the conversion rates for different currency types
        conversion_rates = {
            'USD': {
                'EUR': 0.85,
                'GBP': 0.73,
                'JPY': 109.78
            },
            'EUR': {
                'USD': 1.18,
                'GBP': 0.86,
                'JPY': 130.12
            },
            'GBP': {
                'USD': 1.37,
                'EUR': 1.16,
                'JPY': 151.32
            },
            'JPY': {
                'USD': 0.0091,
                'EUR': 0.0077,
                'GBP': 0.0066
            }
        }
    
        # Check if the given currency types are valid
        if from_currency not in conversion_rates or to_currency not in conversion_rates:
            return "Invalid currency type"
    
        # Convert the value to the desired currency type
        converted_value = amount * conversion_rates[from_currency][to_currency]
        return converted_value