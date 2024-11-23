class DataStatistics:
    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        sorted_data = sorted(data)
        length = len(sorted_data)
        if length % 2 == 0:
            median1 = sorted_data[length // 2]
            median2 = sorted_data[length // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = sorted_data[length // 2]
        return round(median, 2)