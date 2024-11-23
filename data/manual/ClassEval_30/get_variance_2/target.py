class DataStatistics2:
    def get_variance(self):
        """
        Calculate variance, accurate to two digits after the Decimal separator
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_variance()
        1.25
        """
        variance = statistics.variance(self.data)
        variance = round(variance, 2)
        return variance
