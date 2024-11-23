class MetricsCalculator:
    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.precision([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        true_positives = 0
        false_positives = 0
        for pred, true in zip(predicted_labels, true_labels):
            if pred == 1 and true == 1:
                true_positives += 1
            elif pred == 1 and true == 0:
                false_positives += 1
        if true_positives + false_positives == 0:
            return 0
        else:
            return true_positives / (true_positives + false_positives)