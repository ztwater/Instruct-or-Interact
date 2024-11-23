class Statistics3:
    def z_score(data):
        mean = Statistics3.mean(data)
        stdev = Statistics3.standard_deviation(data)
        z_scores = [(x - mean) / stdev for x in data]
        return z_scores