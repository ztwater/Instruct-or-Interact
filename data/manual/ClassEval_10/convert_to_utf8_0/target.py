class BinaryDataProcessor:
    def convert_to_utf8(self):
        utf8_string = self.binary_string.decode('utf-8')
        return utf8_string