class MetricsCalculator:
    def f1_score(precision, recall):
        if precision + recall == 0:
            return 0
        else:
            return 2 * (precision * recall) / (precision + recall)