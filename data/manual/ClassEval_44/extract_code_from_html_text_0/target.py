class HtmlUtil:
    def extract_code_from_html_text(self, html_text):
        # Use regular expressions to find code snippets within <pre><code> tags
        code_regex = r"<pre><code>(.*?)</code></pre>"
        code_snippets = re.findall(code_regex, html_text, re.DOTALL)
        
        # Return the extracted code snippets
        return code_snippets