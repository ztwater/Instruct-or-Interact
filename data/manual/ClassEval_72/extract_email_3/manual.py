### Method Description:
    def extract_email(self, text):
        """
        Extract all email addresses from the text
        :param text: string, input text
        :return: list of string, All extracted email addresses
        >>> ru = RegexUtils()
        >>> ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
        ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com']
        """

### Solution Code:
    def extract_email(self, text):
        pattern = self.generate_email_pattern()
        return self.findall(pattern, text)

### Source Code:
    def extract_email(text):
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        return emails

### Predicted Code:
    def extract_email(self, text):
        """
        Extract all email addresses from the text
        :param text: string, input text
        :return: list of string, All extracted email addresses
        >>> ru = RegexUtils()
        >>> ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
        ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com']
        """
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        return emails



### Adaptation:
Total number: 4
### Raw Output:
```
import re

class RegexUtils:  
    """
    The class provides to match, find all occurrences, split, and substitute text using regular expressions. It also includes predefined patterns, validating phone numbers and extracting email addresses.
    """

    def extract_email(self, text):
        """
        Extract all email addresses from the text
        :param text: string, input text
        :return: list of string, All extracted email addresses
        >>> ru = RegexUtils()
        >>> ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
        ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com']
        """
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        return emails


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

    def generate_phone_number_pattern(self):
        pass

    def generate_split_sentences_pattern(self):
        pass

    def split_sentences(self, text):
        pass

    def validate_phone_number(self, phone_number):
        pass
```

### Test Code:
class RegexUtilsTestExtractEmail(unittest.TestCase):
    def test_extract_email_1(self):
        ru = RegexUtils()
        res = ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
        self.assertEqual(res, ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com'])

    def test_extract_email_2(self):
        ru = RegexUtils()
        res = ru.extract_email("abcdefg@.com ygusyfysy@126.com wljduyuv@qq.com")
        self.assertEqual(res, ['ygusyfysy@126.com', 'wljduyuv@qq.com'])

    def test_extract_email_3(self):
        ru = RegexUtils()
        res = ru.extract_email("abcdefgiscom ygusyfysy@126.com wljduyuv@qq.com")
        self.assertEqual(res, ['ygusyfysy@126.com', 'wljduyuv@qq.com'])

    def test_extract_email_4(self):
        ru = RegexUtils()
        res = ru.extract_email("abcdefgiscom ygusyfysy126.com wljduyuv@qq.com")
        self.assertEqual(res, ['wljduyuv@qq.com'])

    def test_extract_email_5(self):
        ru = RegexUtils()
        res = ru.extract_email("abcdefgiscom ygusyfysy@.com wljduyuv@qq.com")
        self.assertEqual(res, ['wljduyuv@qq.com'])

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: findall, generate_email_pattern


