class Statistics3:
    def mean(lst):
        if len(lst) == 0:
            return None
        else:
            return sum(lst) / len(lst)