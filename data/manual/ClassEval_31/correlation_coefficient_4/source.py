class DataStatistics4:
    def correlation_coefficient(data1, data2):
        # Calculate the mean of the two datasets
        mean1 = np.mean(data1)
        mean2 = np.mean(data2)
        
        # Calculate the standard deviation of the two datasets
        std1 = np.std(data1)
        std2 = np.std(data2)
        
        # Calculate the covariance of the two datasets
        covariance = np.cov(data1, data2)[0][1]
        
        # Calculate the correlation coefficient
        correlation_coefficient = covariance / (std1 * std2)
        
        return correlation_coefficient