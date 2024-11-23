class NumberWordFormatter:
    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        """
        suffixes = ["", "THOUSAND", "MILLION", "BILLION"]
        return suffixes[i]