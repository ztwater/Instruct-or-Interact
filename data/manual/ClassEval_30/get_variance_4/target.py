class DataStatistics2:
    def get_variance(self):
        """
        Calculate variance, accurate to two digits after the Decimal separator
        :return:float
        """
        variance = statistics.variance(self.data)
        variance = round(variance, 2)
        return variance