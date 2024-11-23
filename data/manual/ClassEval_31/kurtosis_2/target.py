class DataStatistics4:
    def kurtosis(data):
        n = len(data)
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        kurtosis = sum((x - mean) ** 4 for x in data) / (variance ** 2)
        return kurtosis
