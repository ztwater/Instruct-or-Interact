class NumberConverter:
    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        >>> NumberConverter.binary_to_decimal('1010010110110111')
        42423
        """
        decimal = 0
        power = 0
        while binary_num != '0':
            decimal += int(binary_num[-1]) * (2 ** power)
            binary_num = binary_num[:-1]
            power += 1
        return decimal