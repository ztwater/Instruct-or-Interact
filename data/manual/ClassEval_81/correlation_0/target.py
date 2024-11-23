class Statistics3:
    def correlation(x, y):
        n = len(x)
        sum_x = sum(x)
        sum_y = sum([i**2 for i in y])
        sum_xy = sum([i*j for i, j in zip(x, y)])
        
        numerator = n * sum_xy - sum_x * sum_x
        denominator = (n * sum_y - sum_x**2) * (n * sum_y - sum_x**2)
        
        correlation = numerator / denominator
        
        return correlation