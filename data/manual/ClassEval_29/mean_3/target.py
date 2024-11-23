class DataStatistics:
    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mean value
        """
        if len(data) == 0:
            return 0.00
        else:
            total = sum(data)
            average = total / len(data)
            return round(average, 2)