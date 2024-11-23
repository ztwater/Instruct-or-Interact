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
    def __format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break
        :param text: string with consecutive line breaks
        :return: string, replaced text with single line break
        """
        return '\n'.join(line.strip() for line in text.splitlines() if line.strip())


### Adaptation:
Total number: 3
### Raw Output:
import re

class HtmlUtil:  
    """
    This is a class as util for html, supporting for formatting and extracting code from HTML text, including cleaning up the text and converting certain elements into specific marks.
    """

    def __init__(self):
        """
        Initialize a series of labels
        """
        self.SPACE_MARK = '-SPACE-'
        self.JSON_MARK = '-JSON-'
        self.MARKUP_LANGUAGE_MARK = '-MARKUP_LANGUAGE-'
        self.URL_MARK = '-URL-'
        self.NUMBER_MARK = '-NUMBER-'
        self.TRACE_MARK = '-TRACE-'
        self.COMMAND_MARK = '-COMMAND-'
        self.COMMENT_MARK = '-COMMENT-'
        self.CODE_MARK = '-CODE-'

    @staticmethod
    def __format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break
        :param text: string with consecutive line breaks
        :return: string, replaced text with single line break
        """
        return '\n'.join(line.strip() for line in text.splitlines() if line.strip())

    def format_line_html_text(self, html_text):
        pass

    def extract_code_from_html_text(self, html_text):
        pass


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
# 0 errors, 4 failures in 5 runs.
# errors:
# failures:
#     AssertionError:
#         test_format_line_feed_1: 'aaa' != 'aaa\n'
#         test_format_line_feed_2: 'aaa' != 'aaa\n'
#         test_format_line_feed_3: 'aaa\nbbb' != 'aaa\nbbb\n'
#         test_format_line_feed_4: 'ccc' != 'ccc\n'


### Dependencies:
# lib_dependencies: re
# field_dependencies: 
# method_dependencies: 


