class Statistics3:
    def correlation(x, y):
        """
        calculates the correlation of the given lists.
        :param x: the given list, list.
        :param y: the given list, list.
        :return: the correlation of the given lists, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
        1.0

        """
        n = len(x)
        sum_x = sum(x)
        sum_y = sum([i**2 for i in y])
        sum_xy = sum([i*j for i, j in zip(x, y)])
        
        numerator = n * sum_xy - sum_x * sum_x
        denominator = (n * sum_y - sum_x**2) * (n * sum_y - sum_x**2)
        
        correlation = numerator / denominator
        
        return correlation