class Statistics3:
    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]

        """
        # Create a dictionary to store the frequency of each element in the list
        frequency = {}
        
        # Iterate through the list and count the frequency of each element
        for element in data:
            if element in frequency:
                frequency[element] += 1
            else:
                frequency[element] = 1
        
        # Find the element(s) with the maximum frequency
        max_frequency = max(frequency.values())
        mode = [element for element, freq in frequency.items() if freq == max_frequency]
        
        return mode