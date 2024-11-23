class BinaryDataProcessor:
    def clean_non_binary_chars(binary_string):
        cleaned_string = ""
        for char in binary_string:
            if char == '0' or char == '1':
                cleaned_string += char
        return cleaned_string