class BinaryDataProcessor:
    def clean_non_binary_chars(self):
        cleaned_string = ""
        for char in self.binary_string:
            if char == '0' or char == '1':
                cleaned_string += char
        self.binary_string = cleaned_string
