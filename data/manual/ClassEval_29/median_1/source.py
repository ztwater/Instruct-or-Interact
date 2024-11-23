class DataStatistics:
    def median(data):
        sorted_data = sorted(data)
        length = len(sorted_data)
        if length % 2 == 0:
            median1 = sorted_data[length // 2]
            median2 = sorted_data[length // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = sorted_data[length // 2]
        return round(median, 2)