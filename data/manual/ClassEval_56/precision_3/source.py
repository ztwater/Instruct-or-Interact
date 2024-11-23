class MetricsCalculator:
    def precision(true_positives, false_positives):
        if true_positives + false_positives == 0:
            return 0
        else:
            return true_positives / (true_positives + false_positives)