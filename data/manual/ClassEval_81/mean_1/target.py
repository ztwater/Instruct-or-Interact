class Statistics3:
    def mean(data):
        if len(data) == 0:
            return None
        else:
            return sum(data) / len(data)