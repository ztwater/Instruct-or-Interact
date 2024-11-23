class NumberConverter:
    def binary_to_decimal(binary_num):
        decimal = 0
        power = 0
        while binary_num != 0:
            decimal += (binary_num % 10) * (2 ** power)
            binary_num //= 10
            power += 1
        return decimal