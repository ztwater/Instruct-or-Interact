### Method Description:
    def decimal_to_binary(decimal_num):
        """
        Convert a number from decimal format to binary format.
        :param decimal_num: int, decimal number
        :return: str, the binary representation of an integer.
        >>> NumberConverter.decimal_to_binary(42423)
        '1010010110110111'
        """

### Solution Code:
    def decimal_to_binary(decimal_num):
        binary_num = bin(decimal_num)[2:]
        return binary_num

### Source Code:
    def decimal_to_binary(decimal):
        binary = bin(decimal)[2:]
        return binary

### Predicted Code:
    def decimal_to_binary(decimal_num):
        binary = bin(decimal_num)[2:]
        return binary

### Adaptation:
Total number: 2
### Raw Output:
class NumberConverter:

    def binary_to_decimal(binary_num):
        pass

    def decimal_to_octal(decimal_num):
        pass

    def octal_to_decimal(octal_num):
        pass

    def decimal_to_hex(decimal_num):
        pass

    def hex_to_decimal(hex_num):
        pass

    @staticmethod
    def decimal_to_binary(decimal_num):
        binary = bin(decimal_num)[2:]
        return binary

### Test Code:
class NumberConverterTestDecimalToBinary(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual('1010010110110111', NumberConverter.decimal_to_binary(42423))

    def test_decimal_to_binary_2(self):
        self.assertEqual('101001100010111', NumberConverter.decimal_to_binary(21271))

    def test_decimal_to_binary_3(self):
        self.assertEqual('1010010111010111', NumberConverter.decimal_to_binary(42455))

    def test_decimal_to_binary_4(self):
        self.assertEqual('10100101110101011', NumberConverter.decimal_to_binary(84907))

    def test_decimal_to_binary_5(self):
        self.assertEqual('101001011101010111', NumberConverter.decimal_to_binary(169815))

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


