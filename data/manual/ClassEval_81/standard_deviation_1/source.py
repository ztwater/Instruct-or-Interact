class Statistics3:
    def standard_deviation(lst):
        n = len(lst)
        mean = sum(lst) / n
        variance = sum((x - mean) ** 2 for x in lst) / n
        std_deviation = math.sqrt(variance)
        return std_deviation