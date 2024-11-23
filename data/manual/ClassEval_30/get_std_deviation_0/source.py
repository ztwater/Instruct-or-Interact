class DataStatistics2:
    def get_std_deviation(numbers):
        n = len(numbers)
        mean = sum(numbers) / n
        variance = sum((x - mean) ** 2 for x in numbers) / n
        std_deviation = math.sqrt(variance)
        std_deviation = round(std_deviation, 2)
        return std_deviation