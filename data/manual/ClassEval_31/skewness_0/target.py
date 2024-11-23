class DataStatistics4:
    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list.
        :return: The skewness, float.
        >>> DataStatistics4.skewness([1, 2, 5])
        2.3760224064818463
        """
        mean = np.mean(data)
        std = np.std(data)
        n = len(data)
        
        skewness = sum((x - mean) ** 3 for x in data) * n / ((n - 1) * (n - 2) * std ** 3)
        
        return skewness