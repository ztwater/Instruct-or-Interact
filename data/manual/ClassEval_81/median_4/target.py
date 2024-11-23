class Statistics3:
    def median(self, data):
        """
        calculates the median of the given list.
        :param data: the given list, list.
        :return: the median of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.median([1, 2, 3, 4])
        2.5

        """
        sorted_lst = sorted(data)
        length = len(sorted_lst)
        if length % 2 == 0:
            mid1 = sorted_lst[length // 2]
            mid2 = sorted_lst[length // 2 - 1]
            median = (mid1 + mid2) / 2
        else:
            median = sorted_lst[length // 2]
        return median