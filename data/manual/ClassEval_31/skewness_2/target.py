class DataStatistics4:
    def skewness(data):
        mean = np.mean(data)
        std = np.std(data)
        n = len(data)
        
        skewness = sum((x - mean) ** 3 for x in data) * n / ((n - 1) * (n - 2) * std ** 3)
        
        return skewness
