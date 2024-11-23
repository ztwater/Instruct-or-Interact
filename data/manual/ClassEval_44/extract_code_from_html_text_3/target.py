class HtmlUtil:
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