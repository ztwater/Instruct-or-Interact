class DataStatistics:
    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        # Create a Counter object to count the frequency of each element in the data
        frequency = Counter(data)
        
        # Find the element(s) with the highest frequency
        max_frequency = max(frequency.values())
        mode = [element for element, freq in frequency.items() if freq == max_frequency]
        
        return mode