class DataStatistics:
    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mean value
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """
        if len(data) == 0:
            return 0.00
        else:
            total = sum(data)
            average = total / len(data)
            return round(average, 2)
