### Method Description:
    def format_line_html_text(self, html_text):
        """
        get the html text without the code, and add the code tag -CODE- where the code is
        :param html_text:string
        :return:string
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.format_line_html_text(<html>
        >>> <body>
        >>>    <h1>Title</h1>
        >>>    <p>This is a paragraph.</p>
        >>>    <pre>print('Hello, world!')</pre>
        >>>    <p>Another paragraph.</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        Title
        This is a paragraph.
        -CODE-
        Another paragraph.
        -CODE-
        """

### Solution Code:
    def format_line_html_text(self, html_text):
        if html_text is None or len(html_text) == 0:
            return ''
        soup = BeautifulSoup(html_text, 'lxml')

        code_tag = soup.find_all(name=['pre', 'blockquote'])
        for tag in code_tag:
            tag.string = self.CODE_MARK

        ul_ol_group = soup.find_all(name=['ul', 'ol'])
        for ul_ol_item in ul_ol_group:
            li_group = ul_ol_item.find_all('li')
            for li_item in li_group:
                li_item_text = li_item.get_text().strip()
                if len(li_item_text) == 0:
                    continue
                if li_item_text[-1] in string.punctuation:
                    li_item.string = '[{0}]{1}'.format('-', li_item_text)
                    continue
                li_item.string = '[{0}]{1}.'.format('-', li_item_text)

        p_group = soup.find_all(name=['p'])
        for p_item in p_group:
            p_item_text = p_item.get_text().strip()
            if p_item_text:
                if p_item_text[-1] in string.punctuation:
                    p_item.string = p_item_text
                    continue
                next_sibling = p_item.find_next_sibling()
                if next_sibling and self.CODE_MARK in next_sibling.get_text():
                    p_item.string = p_item_text + ':'
                    continue
                p_item.string = p_item_text + '.'

        clean_text = gensim.utils.decode_htmlentities(soup.get_text())
        return self.__format_line_feed(clean_text)

### Source Code:
    def format_line_html_text(html_text):
        # Initialize an empty string to store the formatted text
        formatted_text = ""
    
        # Split the html text into lines
        lines = html_text.split("\n")
    
        # Iterate over each line
        for line in lines:
            # Check if the line contains code
            if "<code>" in line:
                # Add the code tag -CODE- to the line
                formatted_text += line.replace("<code>", "-CODE-")
            else:
                # Add the line as it is to the formatted text
                formatted_text += line
    
            # Add a newline character after each line
            formatted_text += "\n"
    
        # Return the formatted text
        return formatted_text

### Predicted Code:
    def format_line_html_text(self, html_text):
        # Initialize an empty string to store the formatted text
        formatted_text = ""
    
        # Split the html text into lines
        lines = html_text.split("\n")
    
        # Iterate over each line
        for line in lines:
            # Check if the line contains code
            if "<code>" in line:
                # Add the code tag -CODE- to the line
                formatted_text += line.replace("<code>", self.CODE_MARK)
            else:
                # Add the line as it is to the formatted text
                formatted_text += line
    
            # Add a newline character after each line
            formatted_text += "\n"
    
        # Return the formatted text
        return formatted_text

### Adaptation:
Total number: 3
### Raw Output:
```python
    def format_line_html_text(self, html_text):
        # Initialize an empty string to store the formatted text
        formatted_text = ""
    
        # Split the html text into lines
        lines = html_text.split("\n")
    
        # Iterate over each line
        for line in lines:
            # Check if the line contains code
            if "<code>" in line:
                # Add the code tag -CODE- to the line
                formatted_text += line.replace("<code>", self.CODE_MARK)
            else:
                # Add the line as it is to the formatted text
                formatted_text += line
    
            # Add a newline character after each line
            formatted_text += "\n"
    
        # Return the formatted text
        return formatted_text
```

### Test Code:
class HtmlUtilTestFormatLineHtmlText(unittest.TestCase):
    def test_format_line_html_text_1(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''
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
        self.assertEqual(res, '''
Title
This is a paragraph.
-CODE-
Another paragraph.
-CODE-
''')

    def test_format_line_html_text_2(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''
        <html>
        <body>
        <h1>Title2</h1>
        <p>This is a paragraph.</p>
        <pre>print('Hello, world!')</pre>
        <p>Another paragraph.</p>
        <pre><code>for i in range(5):
        print(i)</code></pre>
        </body>
        </html>
        ''')
        self.assertEqual(res, '''
Title2
This is a paragraph.
-CODE-
Another paragraph.
-CODE-
''')

    def test_format_line_html_text_3(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''
        <html>
        <body>
        <h1>Title3</h1>
        <p>This is a paragraph.</p>
        <pre>print('Hello, world!')</pre>
        <p>Another paragraph.</p>
        <pre><code>for i in range(5):
        print(i)</code></pre>
        </body>
        </html>
        ''')
        self.assertEqual(res, '''
Title3
This is a paragraph.
-CODE-
Another paragraph.
-CODE-
''')

    def test_format_line_html_text_4(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''
        <html>
        <body>
        <h1>Title4</h1>
        <p>This is a paragraph.</p>
        <pre>print('Hello, world!')</pre>
        <p>Another paragraph.</p>
        <pre><code>for i in range(5):
        print(i)</code></pre>
        </body>
        </html>
        ''')
        self.assertEqual(res, '''
Title4
This is a paragraph.
-CODE-
Another paragraph.
-CODE-
''')

    def test_format_line_html_text_5(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''
        <html>
        <body>
        <h1>Title5</h1>
        <p>This is a paragraph.</p>
        <pre>print('Hello, world!')</pre>
        <p>Another paragraph.</p>
        <pre><code>for i in range(5):
        print(i)</code></pre>
        </body>
        </html>
        ''')
        self.assertEqual(res, '''
Title5
This is a paragraph.
-CODE-
Another paragraph.
-CODE-
''')
    def test_format_line_html_text_6(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('')
        self.assertEqual(res, '')

    def test_format_line_html_text_7(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''<ul><li>Item 1!</li></ul>''')
        self.assertEqual(res, '''[-]Item 1!''')

    def test_format_line_html_text_8(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''<ul><li></li></ul>''')
        self.assertEqual(res, '')

    def test_format_line_html_text_9(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''<p>Some sentence here.</p>''')
        self.assertEqual(res, 'Some sentence here.')

    def test_format_line_html_text_10(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''<p>Some paragraph here</p><code>Code block</code>''')
        self.assertEqual(res, '''Some paragraph here.Code block''')

    def test_format_line_html_text_11(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''<p>Some paragraph here</p><div>Some text here</div>''')
        self.assertEqual(res, '''Some paragraph here.Some text here''')

    def test_format_line_html_text_12(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''<ul><li>Item 1</li></ul>''')
        self.assertEqual(res, '''[-]Item 1.''')

### Test Output:
# 0 errors, 12 failures in 12 runs.
# errors:
# failures:
#     AssertionError:
#         test_format_line_html_text_1: "\n        <html>\n        <body>\n      [243 chars]  \n" != '\nTitle\nThis is a paragraph.\n-CODE-\nA[23 chars]E-\n'
#         test_format_line_html_text_10: '<p>Some paragraph here</p>-CODE-Code block</code>\n' != 'Some paragraph here.Code block'
#         test_format_line_html_text_11: '<p>Some paragraph here</p><div>Some text here</div>\n' != 'Some paragraph here.Some text here'
#         test_format_line_html_text_12: '<ul><li>Item 1</li></ul>\n' != '[-]Item 1.'
#         test_format_line_html_text_2: "\n        <html>\n        <body>\n      [244 chars]  \n" != '\nTitle2\nThis is a paragraph.\n-CODE-\n[24 chars]E-\n'
#         test_format_line_html_text_3: "\n        <html>\n        <body>\n      [244 chars]  \n" != '\nTitle3\nThis is a paragraph.\n-CODE-\n[24 chars]E-\n'
#         test_format_line_html_text_4: "\n        <html>\n        <body>\n      [244 chars]  \n" != '\nTitle4\nThis is a paragraph.\n-CODE-\n[24 chars]E-\n'
#         test_format_line_html_text_5: "\n        <html>\n        <body>\n      [244 chars]  \n" != '\nTitle5\nThis is a paragraph.\n-CODE-\n[24 chars]E-\n'
#         test_format_line_html_text_6: '\n' != ''
#         test_format_line_html_text_7: '<ul><li>Item 1!</li></ul>\n' != '[-]Item 1!'
#         test_format_line_html_text_8: '<ul><li></li></ul>\n' != ''
#         test_format_line_html_text_9: '<p>Some sentence here.</p>\n' != 'Some sentence here.'


### Dependencies:
# lib_dependencies: string, gensim, BeautifulSoup
# field_dependencies: self.CODE_MARK
# method_dependencies: __format_line_feed


