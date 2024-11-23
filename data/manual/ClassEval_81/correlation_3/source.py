class Statistics3:
    def correlation(lst):
        n = len(lst)
        sum_x = sum(lst)
        sum_y = sum([i**2 for i in lst])
        sum_xy = sum([i*j for i, j in zip(lst, lst)])
        
        numerator = n * sum_xy - sum_x * sum_x
        denominator = (n * sum_y - sum_x**2) * (n * sum_y - sum_x**2)
        
        correlation = numerator / denominator
        
        return correlation