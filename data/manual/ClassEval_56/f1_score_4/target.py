class MetricsCalculator:
    def f1_score(self, predicted_labels, true_labels):
        """
        Calculate f1 score, which is the harmonic mean of precision and recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        p = self.precision(predicted_labels, true_labels)
        r = self.recall(predicted_labels, true_labels)

        if p + r == 0:
            return 0
        else:
            return 2 * (p * r) / (p + r)