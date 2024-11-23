### Method Description:
    @staticmethod
    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        >>> NumberConverter.binary_to_decimal('1010010110110111')
        42423
        """

### Solution Code:
    @staticmethod
    def binary_to_decimal(binary_num):
        decimal_num = int(binary_num, 2)
        return decimal_num

### Source Code:
    def binary_to_decimal(binary):
        decimal = 0
        power = 0
        while binary != 0:
            decimal += (binary % 10) * (2 ** power)
            binary //= 10
            power += 1
        return decimal

### Predicted Code:
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
        while binary_num != "":
            decimal += int(binary_num[-1]) * (2 ** power)
            binary_num = binary_num[:-1]
            power += 1
        return decimal

### Adaptation:
Total number: 20
### Raw Output:
```
    @staticmethod
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
        while binary_num != "":
            decimal += int(binary_num[-1]) * (2 ** power)
            binary_num = binary_num[:-1]
            power += 1
        return decimal
```

### Test Code:
class NumberConverterTestBinaryToDecimal(unittest.TestCase):
    def test_binary_to_decimal(self):
        self.assertEqual(42423, NumberConverter.binary_to_decimal('1010010110110111'))

    def test_binary_to_decimal_2(self):
        self.assertEqual(10615, NumberConverter.binary_to_decimal('10100101110111'))

    def test_binary_to_decimal_3(self):
        self.assertEqual(42455, NumberConverter.binary_to_decimal('1010010111010111'))

    def test_binary_to_decimal_4(self):
        self.assertEqual(169819, NumberConverter.binary_to_decimal('101001011101011011'))

    def test_binary_to_decimal_5(self):
        self.assertEqual(339639, NumberConverter.binary_to_decimal('1010010111010110111'))

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


