class HtmlUtil:
    def __format_line_feed(self, text):
        return '\n'.join(line.strip() for line in text.splitlines() if line.strip())