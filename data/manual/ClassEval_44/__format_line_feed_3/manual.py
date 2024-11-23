### Method Description:
    def __format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break
        :param text: string with consecutive line breaks
        :return:string, replaced text with single line break
        """

### Solution Code:
    def __format_line_feed(text):
        return re.sub(re.compile(r'\n+'), '\n', text)

### Source Code:
    def __format_line_feed(text):
        return '\n'.join(line.strip() for line in text.splitlines() if line.strip())

### Predicted Code:
    def __format_line_feed(self, text):
        return '\n'.join(line.strip() for line in text.splitlines() if line.strip())

### Adaptation:
Total number: 1
### Raw Output:
```
    def __format_line_feed(self, text):
        return '\n'.join(line.strip() for line in text.splitlines() if line.strip())
```

### Test Code:
class HtmlUtilTestFormatLineFeed(unittest.TestCase):
    def test_format_line_feed_1(self):
        self.assertEqual(HtmlUtil._HtmlUtil__format_line_feed('aaa\n\n\n'), 'aaa\n')

    def test_format_line_feed_2(self):
        self.assertEqual(HtmlUtil._HtmlUtil__format_line_feed('aaa\n\n\n\n'), 'aaa\n')

    def test_format_line_feed_3(self):
        self.assertEqual(HtmlUtil._HtmlUtil__format_line_feed('aaa\n\n\nbbb\n\n'), 'aaa\nbbb\n')

    def test_format_line_feed_4(self):
        self.assertEqual(HtmlUtil._HtmlUtil__format_line_feed('ccc\n\n\n'), 'ccc\n')

    def test_format_line_feed_5(self):
        self.assertEqual(HtmlUtil._HtmlUtil__format_line_feed(''), '')

### Test Output:
# 5 errors, 0 failures in 5 runs.
# errors:
#     TypeError:
#         test_format_line_feed_1: __format_line_feed() missing 1 required positional argument: 'text'
#         test_format_line_feed_2: __format_line_feed() missing 1 required positional argument: 'text'
#         test_format_line_feed_3: __format_line_feed() missing 1 required positional argument: 'text'
#         test_format_line_feed_4: __format_line_feed() missing 1 required positional argument: 'text'
#         test_format_line_feed_5: __format_line_feed() missing 1 required positional argument: 'text'
# failures:


### Dependencies:
# lib_dependencies: re
# field_dependencies: 
# method_dependencies: 


