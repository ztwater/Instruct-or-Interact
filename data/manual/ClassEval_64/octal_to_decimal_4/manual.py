### Method Description:
    @staticmethod
    def octal_to_decimal(octal_num):
        """
        Convert a number from octal format to decimal format.
        :param octal_num: str, octal num
        :return: int, the decimal representation of octal number str.
        >>> NumberConverter.octal_to_decimal('122667')
        42423
        """

### Solution Code:
    @staticmethod
    def octal_to_decimal(octal_num):
        decimal_num = int(octal_num, 8)
        return decimal_num

### Source Code:
    def octal_to_decimal(octal_number):
        decimal_number = 0
        power = 0
        
        while octal_number != 0:
            last_digit = octal_number % 10
            decimal_number += last_digit * (8 ** power)
            octal_number //= 10
            power += 1
        
        return decimal_number

### Predicted Code:
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

### Adaptation:
Total number: 13
### Raw Output:
```python
class NumberConverter:  
    """
    The class allows to convert decimal to binary, octal and hexadecimal respectively and contrarily
    """

    @staticmethod
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
```

### Test Code:
class NumberConvertTestOctalToDecimal(unittest.TestCase):
    def test_octal_to_decimal(self):
        self.assertEqual(42423, NumberConverter.octal_to_decimal('122667'))

    def test_octal_to_decimal_2(self):
        self.assertEqual(21271, NumberConverter.octal_to_decimal('51427'))

    def test_octal_to_decimal_3(self):
        self.assertEqual(84907, NumberConverter.octal_to_decimal('245653'))

    def test_octal_to_decimal_4(self):
        self.assertEqual(169815, NumberConverter.octal_to_decimal('513527'))

    def test_octal_to_decimal_5(self):
        self.assertEqual(339630, NumberConverter.octal_to_decimal('1227256'))

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


