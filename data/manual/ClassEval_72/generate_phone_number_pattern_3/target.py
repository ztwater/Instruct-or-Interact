class RegexUtils:
    def generate_phone_number_pattern(self):
        """
        Generate regular expression patterns that match phone numbers
        :return: string, regular expression patterns that match phone numbers
        >>> ru = RegexUtils()
        >>> ru.generate_phone_number_pattern()
        '\b\d{3}-\d{3}-\d{4}\b'
        """
        # Regular expression pattern for phone numbers
        pattern = r'\b\d{3}-\d{3}-\d{4}\b'
        
        return pattern