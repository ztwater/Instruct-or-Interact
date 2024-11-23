class Statistics3:
    def median(self, data):
        sorted_data = sorted(data)
        length = len(sorted_data)
        if length % 2 == 0:
            mid1 = sorted_data[length // 2]
            mid2 = sorted_data[length // 2 - 1]
            median = (mid1 + mid2) / 2
        else:
            median = sorted_data[length // 2]
        return median
