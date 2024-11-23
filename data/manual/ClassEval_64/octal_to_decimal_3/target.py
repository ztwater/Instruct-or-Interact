class NumberConverter:
    def octal_to_decimal(octal_num):
        decimal_number = 0
        power = 0

        while octal_num != '0':
            last_digit = int(octal_num[-1])
            decimal_number += last_digit * (8 ** power)
            octal_num = octal_num[:-1]
            power += 1

        return decimal_number