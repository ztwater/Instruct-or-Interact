class NumericEntityUnescaper:
    def is_hex_char(self, char):
        """
        Determines whether a given character is a hexadecimal digit.
        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        >>> NumericEntityUnescaper().is_hex_char('a')
        True

        """
        hex_digits = "0123456789ABCDEF"
        return char.upper() in hex_digits