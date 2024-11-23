class MetricsCalculator:
    def recall(self, predicted_labels, true_labels):
        true_positives = 0
        false_negatives = 0
        for pred, true in zip(predicted_labels, true_labels):
            if pred == true == 1:
                true_positives += 1
            elif pred == 0 and true == 1:
                false_negatives += 1
        recall = true_positives / (true_positives + false_negatives)
        return recall