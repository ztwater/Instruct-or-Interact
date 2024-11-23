class Statistics3:
    def mode(data):
        frequency = {}
        
        for element in data:
            if element in frequency:
                frequency[element] += 1
            else:
                frequency[element] = 1
        
        max_frequency = max(frequency.values())
        mode = [element for element, freq in frequency.items() if freq == max_frequency]
        
        return mode
