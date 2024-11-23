class DataStatistics2:
    def get_variance(self):
        variance = np.var(self.data)
        variance = round(variance, 2)
        return variance