class DataStatistics2:
    def get_correlation(self):
        """
        Calculate correlation
        :return:float
        """
        # Calculate the mean of each list
        mean1 = np.mean(self.data)
        mean2 = np.mean(self.data)
        
        # Calculate the numerator and denominator of the correlation formula
        numerator = np.sum((x - mean1) * (y - mean2) for x, y in zip(self.data, self.data))
        denominator = (np.sum((x - mean1) ** 2 for x in self.data) * np.sum((y - mean2) ** 2 for y in self.data)) ** 0.5
        
        # Calculate the correlation coefficient
        correlation = numerator / denominator
        
        return correlation