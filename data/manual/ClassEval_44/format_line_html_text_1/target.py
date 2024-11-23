class HtmlUtil:
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