class HtmlUtil:
    def extract_code_from_html_text(html_text):
        # Use regular expressions to find code snippets within <code> tags
        code_regex = r"<code>(.*?)</code>"
        code_snippets = re.findall(code_regex, html_text, re.DOTALL)
        
        # Return the extracted code snippets
        return code_snippets