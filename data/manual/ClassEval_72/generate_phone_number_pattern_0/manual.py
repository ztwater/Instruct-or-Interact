### Method Description:
    def generate_phone_number_pattern(self):
        """
        Generate regular expression patterns that match phone numbers
        :return: string, regular expression patterns that match phone numbers
        >>> ru = RegexUtils()
        >>> ru.generate_phone_number_pattern()
        '\b\d{3}-\d{3}-\d{4}\b'
        """

### Solution Code:
    def generate_phone_number_pattern(self):
        pattern = r'\b\d{3}-\d{3}-\d{4}\b'
        return pattern

### Source Code:
    def generate_phone_number_pattern():
        # Regular expression pattern for phone numbers
        pattern = r'^\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}$'
        
        return pattern

### Predicted Code:
    def generate_phone_number_pattern(self):
        """
        Generate regular expression patterns that match phone numbers
        :return: string, regular expression patterns that match phone numbers
        """
        pattern = r'\b\d{3}-\d{3}-\d{4}\b'
        return pattern


### Adaptation:
Total number: 5
### Raw Output:
To adapt the provided method `generate_phone_number_pattern` to the class context of `RegexUtils`, you can rewrite the method as follows:

```python
import re
class RegexUtils:
    """
    The class provides to match, find all occurrences, split, and substitute text using regular expressions. It also includes predefined patterns, validating phone numbers and extracting email addresses.
    """

    def generate_phone_number_pattern(self):
        """
        Generate regular expression patterns that match phone numbers
        :return: string, regular expression patterns that match phone numbers
        """
        pattern = r'\b\d{3}-\d{3}-\d{4}\b'
        return pattern

    def match(self, pattern, text):
        pass

    def findall(self, pattern, text):
        pass

    def split(self, pattern, text):
        pass

    def sub(self, pattern, replacement, text):
        pass

    def generate_email_pattern(self):
        pass

    def generate_split_sentences_pattern(self):
        pass

    def split_sentences(self, text):
        pass

    def validate_phone_number(self, phone_number):
        pass

    def extract_email(self, text):
        pass
```

The adapted method `generate_phone_number_pattern` is now included in the `RegexUtils` class and returns the regular expression pattern for matching phone numbers.

### Test Code:
class RegexUtilsTestGeneratePhoneNumberPattern(unittest.TestCase):
    def test_generate_phone_number_pattern_1(self):
        ru = RegexUtils()
        pat = ru.generate_phone_number_pattern()
        res = ru.match(pat, '123-456-7890')
        self.assertEqual(res, True)

    def test_generate_phone_number_pattern_2(self):
        ru = RegexUtils()
        pat = ru.generate_phone_number_pattern()
        res = ru.match(pat, '1234567890')
        self.assertEqual(res, False)

    def test_generate_phone_number_pattern_3(self):
        ru = RegexUtils()
        pat = ru.generate_phone_number_pattern()
        res = ru.match(pat, '123-456-789')
        self.assertEqual(res, False)

    def test_generate_phone_number_pattern_4(self):
        ru = RegexUtils()
        pat = ru.generate_phone_number_pattern()
        res = ru.match(pat, 'a23-456-7890')
        self.assertEqual(res, False)

    def test_generate_phone_number_pattern_5(self):
        ru = RegexUtils()
        pat = ru.generate_phone_number_pattern()
        res = ru.match(pat, '1234-56-7890')
        self.assertEqual(res, False)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


