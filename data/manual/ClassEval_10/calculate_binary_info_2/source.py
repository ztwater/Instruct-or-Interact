class BinaryDataProcessor:
    def calculate_binary_info(binary_string):
        total_length = len(binary_string)
        count_0 = binary_string.count('0')
        count_1 = binary_string.count('1')
        percentage_0 = (count_0 / total_length) * 100
        percentage_1 = (count_1 / total_length) * 100
    
        return {
            'percentage_0': percentage_0,
            'percentage_1': percentage_1,
            'total_length': total_length
        }