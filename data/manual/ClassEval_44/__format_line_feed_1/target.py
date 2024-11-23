class HtmlUtil:
    def __format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break
        :param text: string with consecutive line breaks
        :return: string, replaced text with single line break
        """
        return '\n'.join(line.strip() for line in text.splitlines() if line.strip())
