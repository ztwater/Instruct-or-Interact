### Method Description:
    def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.extract_code_from_html_text(<html>
        >>> <body>
        >>>    <h1>Title</h1>
        >>>    <p>This is a paragraph.</p>
        >>>    <pre>print('Hello, world!')</pre>
        >>>    <p>Another paragraph.</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        ["print('Hello, world!')", 'for i in range(5):\n                print(i)']
        """

### Solution Code:
    def extract_code_from_html_text(self, html_text):
        text_with_code_tag = self.format_line_html_text(html_text)

        if self.CODE_MARK not in text_with_code_tag:
            return []

        code_index_start = 0
        soup = BeautifulSoup(html_text, 'lxml')
        code_tag = soup.find_all(name=['pre', 'blockquote'])
        code_count = text_with_code_tag.count(self.CODE_MARK)
        code_list = []
        for code_index in range(code_index_start, code_index_start + code_count):
            code = code_tag[code_index].get_text()
            if code:
                code_list.append(code)
        return code_list

### Source Code:
    def extract_code_from_html_text(html_text):
        # Use regular expressions to find code snippets within <code> tags
        code_regex = r"<code>(.*?)</code>"
        code_snippets = re.findall(code_regex, html_text, re.DOTALL)
        
        # Return the extracted code snippets
        return code_snippets

### Predicted Code:
    def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        """
        # Use regular expressions to find code snippets within <code> tags
        code_regex = r"<code>(.*?)</code>"
        code_snippets = re.findall(code_regex, html_text, re.DOTALL)
        
        # Return the extracted code snippets
        return code_snippets

### Adaptation:
Total number: 2
### Raw Output:
```
    def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        """
        # Use regular expressions to find code snippets within <code> tags
        code_regex = r"<code>(.*?)</code>"
        code_snippets = re.findall(code_regex, html_text, re.DOTALL)
        
        # Return the extracted code snippets
        return code_snippets
```

### Test Code:
class HtmlUtilTestExtractCodeFromHtmlText(unittest.TestCase):
    def test_extract_code_from_html_text_1(self):
        htmlutil = HtmlUtil()
        res = htmlutil.extract_code_from_html_text('''
                <html>
                <body>
                <h1>Title</h1>
                <p>This is a paragraph.</p>
                <pre>print('Hello, world!')</pre>
                <p>Another paragraph.</p>
                <pre><code>for i in range(5):
                print(i)</code></pre>
                </body>
                </html>
                ''')
        self.assertEqual(res, ["print('Hello, world!')", 'for i in range(5):\n                print(i)'])

    def test_extract_code_from_html_text_2(self):
        htmlutil = HtmlUtil()
        res = htmlutil.extract_code_from_html_text('''
                <html>
                <body>
                <h1>Title</h1>
                <p>This is a paragraph.</p>
                <pre>print('Hello, world!')</pre>
                <p>Another paragraph.</p>
                <pre><code>for i in range(4):
                print(i)</code></pre>
                </body>
                </html>
                ''')
        self.assertEqual(res, ["print('Hello, world!')", 'for i in range(4):\n                print(i)'])

    def test_extract_code_from_html_text_3(self):
        htmlutil = HtmlUtil()
        res = htmlutil.extract_code_from_html_text('''
                <html>
                <body>
                <h1>Title</h1>
                <p>This is a paragraph.</p>
                <pre>print('Hello, world!')</pre>
                <p>Another paragraph.</p>
                <pre><code>for i in range(3):
                print(i)</code></pre>
                </body>
                </html>
                ''')
        self.assertEqual(res, ["print('Hello, world!')", 'for i in range(3):\n                print(i)'])

    def test_extract_code_from_html_text_4(self):
        htmlutil = HtmlUtil()
        res = htmlutil.extract_code_from_html_text('''
                <html>
                <body>
                <h1>Title</h1>
                <p>This is a paragraph.</p>
                <pre>print('Hello, world!')</pre>
                <p>Another paragraph.</p>
                <pre><code>for i in range(2):
                print(i)</code></pre>
                </body>
                </html>
                ''')
        self.assertEqual(res, ["print('Hello, world!')", 'for i in range(2):\n                print(i)'])

    def test_extract_code_from_html_text_5(self):
        htmlutil = HtmlUtil()
        htmlutil.CODE_MARK = 'abcdefg'
        res = htmlutil.extract_code_from_html_text("")
        self.assertEqual(res, [])

### Test Output:
# 0 errors, 4 failures in 5 runs.
# errors:
# failures:
#     AssertionError:
#         test_extract_code_from_html_text_1: Lists differ: ['for i in range(5):\n                print(i)'] != ["print('Hello, world!')", 'for i in range(5):\n                print(i)']
#         test_extract_code_from_html_text_2: Lists differ: ['for i in range(4):\n                print(i)'] != ["print('Hello, world!')", 'for i in range(4):\n                print(i)']
#         test_extract_code_from_html_text_3: Lists differ: ['for i in range(3):\n                print(i)'] != ["print('Hello, world!')", 'for i in range(3):\n                print(i)']
#         test_extract_code_from_html_text_4: Lists differ: ['for i in range(2):\n                print(i)'] != ["print('Hello, world!')", 'for i in range(2):\n                print(i)']


### Dependencies:
# lib_dependencies: BeautifulSoup
# field_dependencies: self.CODE_MARK
# method_dependencies: format_line_html_text


