class MetricsCalculator:
    def recall(true_positives, false_negatives):
        recall = true_positives / (true_positives + false_negatives)
        return recall