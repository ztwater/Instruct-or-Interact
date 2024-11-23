class NumericEntityUnescaper:
    def replace(self, string):
        return html.unescape(string)