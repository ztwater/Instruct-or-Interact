class MetricsCalculator:
    def recall(self, predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        true_positives = 0
        false_negatives = 0
        for i in range(len(predicted_labels)):
            if predicted_labels[i] == 1 and true_labels[i] == 1:
                true_positives += 1
            elif predicted_labels[i] == 0 and true_labels[i] == 1:
                false_negatives += 1
        recall = true_positives / (true_positives + false_negatives)
        return recall