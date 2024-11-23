class Statistics3:
    def mode(lst):
        # Create a dictionary to store the frequency of each element in the list
        frequency = {}
        
        # Iterate through the list and count the frequency of each element
        for element in lst:
            if element in frequency:
                frequency[element] += 1
            else:
                frequency[element] = 1
        
        # Find the element(s) with the maximum frequency
        max_frequency = max(frequency.values())
        mode = [element for element, freq in frequency.items() if freq == max_frequency]
        
        return mode