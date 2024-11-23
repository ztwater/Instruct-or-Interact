class BinaryDataProcessor:
    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        """
        utf8_string = self.binary_string.decode('utf-8')
        return utf8_string