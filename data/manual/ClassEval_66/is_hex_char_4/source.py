class NumericEntityUnescaper:
    def is_hex_char(char):
        hex_digits = "0123456789ABCDEF"
        return char.upper() in hex_digits