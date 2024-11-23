class DataStatistics2:
    def get_std_deviation(self):
        """
        Calculate standard deviation, accurate to two digits after the Decimal separator
        :return: float
        """
        n = len(self.data)
        mean = np.mean(self.data)
        variance = np.var(self.data)
        std_deviation = math.sqrt(variance)
        std_deviation = round(std_deviation, 2)
        return std_deviation
