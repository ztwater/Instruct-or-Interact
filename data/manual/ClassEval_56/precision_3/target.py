class MetricsCalculator:
    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        true_positives = 0
        false_positives = 0
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                true_positives += 1
            elif predicted == 1 and true == 0:
                false_positives += 1
        if true_positives + false_positives == 0:
            return 0
        else:
            return true_positives / (true_positives + false_positives)