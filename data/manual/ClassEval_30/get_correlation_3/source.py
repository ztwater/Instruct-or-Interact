class DataStatistics2:
    def get_correlation(list1, list2):
        # Calculate the mean of each list
        mean1 = sum(list1) / len(list1)
        mean2 = sum(list2) / len(list2)
        
        # Calculate the numerator and denominator of the correlation formula
        numerator = sum((x - mean1) * (y - mean2) for x, y in zip(list1, list2))
        denominator = (sum((x - mean1) ** 2 for x in list1) * sum((y - mean2) ** 2 for y in list2)) ** 0.5
        
        # Calculate the correlation coefficient
        correlation = numerator / denominator
        
        return correlation