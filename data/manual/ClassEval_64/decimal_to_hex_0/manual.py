### Method Description:
    @staticmethod
    def decimal_to_hex(decimal_num):
        """
        Convert a number from decimal format to hex format.
        :param decimal_num: int, decimal number
        :return hex_num: str, the hex representation of an integer.
        >>> NumberConverter.decimal_to_hex(42423)
        'a5b7'
        """

### Solution Code:
    @staticmethod
    def decimal_to_hex(decimal_num):
        hex_num = hex(decimal_num)[2:]
        return hex_num

### Source Code:
    def decimal_to_hex(decimal):
        hex_value = hex(decimal)
        return hex_value

### Predicted Code:
    def decimal_to_hex(decimal_num):
        hex_num = hex(decimal_num)[2:]
        return hex_num


### Adaptation:
Total number: 7
### Raw Output:
```python
class NumberConverter:  
    """
    The class allows to convert decimal to binary, octal and hexadecimal respectively and contrarily
    """

    @staticmethod
    def decimal_to_hex(decimal_num):
        hex_num = hex(decimal_num)[2:]
        return hex_num

    def decimal_to_binary(decimal_num):
        pass

    def binary_to_decimal(binary_num):
        pass

    def decimal_to_octal(decimal_num):
        pass

    def octal_to_decimal(octal_num):
        pass

    def hex_to_decimal(hex_num):
        pass
```

### Test Code:
class NumberConvertTestDecimalToHex(unittest.TestCase):
    def test_decimal_to_hex(self):
        self.assertEqual('a5b7', NumberConverter.decimal_to_hex(42423))

    def test_decimal_to_hex_2(self):
        self.assertEqual('5317', NumberConverter.decimal_to_hex(21271))

    def test_decimal_to_hex_3(self):
        self.assertEqual('14bab', NumberConverter.decimal_to_hex(84907))

    def test_decimal_to_hex_4(self):
        self.assertEqual('29757', NumberConverter.decimal_to_hex(169815))

    def test_decimal_to_hex_5(self):
        self.assertEqual('52eb7', NumberConverter.decimal_to_hex(339639))

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


