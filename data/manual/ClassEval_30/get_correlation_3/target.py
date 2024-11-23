class DataStatistics2:
    def get_correlation(self):
        """
        Calculate correlation
        :return:float
        """
        list1 = self.data
        list2 = self.data
        
        # Calculate the mean of each list
        mean1 = np.mean(list1)
        mean2 = np.mean(list2)
        
        # Calculate the numerator and denominator of the correlation formula
        numerator = np.sum((x - mean1) * (y - mean2) for x, y in zip(list1, list2))
        denominator = (np.sum((x - mean1) ** 2 for x in list1) * np.sum((y - mean2) ** 2 for y in list2)) ** 0.5
        
        # Calculate the correlation coefficient
        correlation = numerator / denominator
        
        return correlation