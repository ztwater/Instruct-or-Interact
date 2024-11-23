class HtmlUtil:
    def format_line_html_text(self, html_text):
        # Initialize an empty string to store the formatted text
        formatted_text = ""
    
        # Split the html text into lines
        lines = html_text.split("\n")
    
        # Iterate over each line
        for line in lines:
            # Check if the line contains code
            if "<pre><code>" in line:
                # Add the code tag -CODE- to the line
                formatted_text += line.replace("<pre><code>", self.CODE_MARK)
            elif "</code></pre>" in line:
                # Add the code tag -CODE- to the line
                formatted_text += self.CODE_MARK
            else:
                # Add the line as it is to the formatted text
                formatted_text += line
    
            # Add a newline character after each line
            formatted_text += "\n"
    
        # Return the formatted text
        return formatted_text