class NumberConverter:
    def octal_to_decimal(octal_number):
        decimal_number = 0
        power = 0
        
        while octal_number != 0:
            last_digit = octal_number % 10
            decimal_number += last_digit * (8 ** power)
            octal_number //= 10
            power += 1
        
        return decimal_number