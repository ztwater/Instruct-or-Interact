class DataStatistics:
    def mode(self, data):
        # Create a counter object to store the frequency of each element in the data
        frequency = Counter(data)
        
        # Find the element(s) with the highest frequency
        max_frequency = max(frequency.values())
        mode = [element for element, freq in frequency.items() if freq == max_frequency]
        
        return mode