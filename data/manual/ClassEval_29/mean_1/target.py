class DataStatistics:
    def mean(self, data):
        if len(data) == 0:
            return 0.00
        else:
            total = sum(data)
            average = total / len(data)
            return round(average, 2)
