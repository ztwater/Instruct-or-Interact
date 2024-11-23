class NumberWordFormatter:
    def format(self, x):
        """
        Converts a number into words format
        :param x: int or float, the number to be converted into words format
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        number = str(x)   # Convert number to string
        
        # Split the number into integer and decimal parts
        integer_part = number.split('.')[0]
        decimal_part = number.split('.')[1] if len(number.split('.')) > 1 else '0'
        
        int_word = self.format_string(int(integer_part))   # Convert integer part to word format
        
        # Convert decimal part to word format
        decimal_word = ''
        if decimal_part != '0':
            decimal_word = 'POINT '
            for digit in decimal_part:
                decimal_word += self.format_string(int(digit)) + ' '
        
        # Combine the integer and decimal parts with appropriate connectors and units
        words = int_word + ' ' + decimal_word + 'ONLY'
        return words