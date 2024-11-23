class NumberConverter:
    def octal_to_decimal(octal_num):
        """
        Convert a number from octal format to decimal format.
        :param octal_num: str, octal num
        :return: int, the decimal representation of octal number str.
        >>> NumberConverter.octal_to_decimal('122667')
        42423
        """
        decimal_number = 0
        power = 0
        
        while octal_num != 0:
            last_digit = int(octal_num) % 10
            decimal_number += last_digit * (8 ** power)
            octal_num = int(octal_num) // 10
            power += 1
        
        return decimal_number