class Statistics3:
    def median(lst):
        sorted_lst = sorted(lst)
        length = len(sorted_lst)
        if length % 2 == 0:
            mid1 = sorted_lst[length // 2]
            mid2 = sorted_lst[length // 2 - 1]
            median = (mid1 + mid2) / 2
        else:
            median = sorted_lst[length // 2]
        return median