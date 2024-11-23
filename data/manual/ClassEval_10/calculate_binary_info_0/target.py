class BinaryDataProcessor:
    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        """
        total_length = len(self.binary_string)
        count_0 = self.binary_string.count('0')
        count_1 = self.binary_string.count('1')
        percentage_0 = (count_0 / total_length) * 100
        percentage_1 = (count_1 / total_length) * 100
    
        return {
            'Zeroes': percentage_0,
            'Ones': percentage_1,
            'Bit length': total_length
        }