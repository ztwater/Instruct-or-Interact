class BinaryDataProcessor:
    def convert_to_ascii(binary_string):
        # Split the binary string into groups of 8 characters
        binary_groups = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
        
        # Convert each binary group to its corresponding ASCII character
        ascii_string = ''.join([chr(int(group, 2)) for group in binary_groups])
        
        return ascii_string