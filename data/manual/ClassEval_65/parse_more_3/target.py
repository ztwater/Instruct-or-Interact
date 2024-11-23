class NumberWordFormatter:
    def parse_more(self, i):
        suffixes = ["", "thousand", "million", "billion"]
        return suffixes[i]