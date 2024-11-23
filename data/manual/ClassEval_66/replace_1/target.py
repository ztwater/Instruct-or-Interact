class NumericEntityUnescaper:
    def replace(self, string):
        import html
    
        return html.unescape(string)