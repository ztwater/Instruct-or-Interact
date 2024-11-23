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
        numerator = np.sum((self.data - mean1) * (self.data - mean2))
        denominator = (np.sum((self.data - mean1) ** 2) * np.sum((self.data - mean2) ** 2)) ** 0.5
        
        # Calculate the correlation coefficient
        correlation = numerator / denominator
        
        return correlation