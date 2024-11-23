class DataStatistics:
    def mode(data):
        # Create a dictionary to store the frequency of each element in the data
        frequency = {}
        
        # Iterate through the data and count the frequency of each element
        for element in data:
            if element in frequency:
                frequency[element] += 1
            else:
                frequency[element] = 1
        
        # Find the element(s) with the highest frequency
        max_frequency = max(frequency.values())
        mode = [element for element, freq in frequency.items() if freq == max_frequency]
        
        return mode