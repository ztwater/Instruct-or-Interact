class Statistics3:
    def z_score(lst):
        mean = statistics.mean(lst)
        stdev = statistics.stdev(lst)
        z_scores = [(x - mean) / stdev for x in lst]
        return z_scores