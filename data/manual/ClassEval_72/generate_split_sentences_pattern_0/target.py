class RegexUtils:
    def generate_split_sentences_pattern(self):
        """
        Generate regular expression patterns that match the middle characters of two sentences
        :return: string, regular expression patterns that match the middle characters of two sentences
        >>> ru = RegexUtils()
        >>> ru.generate_split_sentences_pattern()
        '[.!?][\s]{1,2}(?=[A-Z])'
        """
        middle1 = r"\w(?<![\s\W])"
        middle2 = r"(?<![\s\W])\w"
        pattern = f"{middle1}{middle2}"
        return pattern