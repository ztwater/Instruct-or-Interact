### Method Description:
    @staticmethod
    def hex_to_decimal(hex_num):
        """
        Convert a number from hex format to decimal format.
        :param hex_num: str, hex num
        :return: int, the decimal representation of hex number str.
        >>> NumberConverter.hex_to_decimal('a5b7')
        42423
        """

### Solution Code:
    @staticmethod
    def hex_to_decimal(hex_num):
        decimal_num = int(hex_num, 16)
        return decimal_num

### Source Code:
    def hex_to_decimal(hex_num):
        decimal_num = int(hex_num, 16)
        return decimal_num

### Predicted Code:


### Adaptation:
Total number: 4
### Raw Output:
```python
class NumberConverter:
    """
    The class allows to convert decimal to binary, octal and hexadecimal respectively and contrarily
    """


    def decimal_to_binary(decimal_num):
        pass

    def binary_to_decimal(binary_num):
        pass

    def decimal_to_octal(decimal_num):
        pass

    def octal_to_decimal(octal_num):
        pass

    def decimal_to_hex(decimal_num):
        hex_num = hex(decimal_num).lstrip("0x")
        return int(hex_num, 16)
```

### Test Code:
class NumberConvertTestHexToDecimal(unittest.TestCase):
    def test_hex_to_decimal(self):
        self.assertEqual(42423, NumberConverter.hex_to_decimal('a5b7'))

    def test_hex_to_decimal_2(self):
        self.assertEqual(21207, NumberConverter.hex_to_decimal('52d7'))

    def test_hex_to_decimal_3(self):
        self.assertEqual(84627, NumberConverter.hex_to_decimal('14a93'))

    def test_hex_to_decimal_4(self):
        self.assertEqual(170615, NumberConverter.hex_to_decimal('29a77'))

    def test_hex_to_decimal_5(self):
        self.assertEqual(342647, NumberConverter.hex_to_decimal('53a77'))

### Test Output:
# Compilation error: {test_output['compilation']}

### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


