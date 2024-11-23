class MetricsCalculator:
    def update(self, predicted_labels, true_labels):
        """
        Update the number of all four samples(true_positives, false_positives, false_negatives, true_negatives)
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: None, change the number of corresponding samples
        """
        for predicted_label, true_label in zip(predicted_labels, true_labels):
            if predicted_label == 1 and true_label == 1:
                self.true_positives += 1
            elif predicted_label == 1 and true_label == 0:
                self.false_positives += 1
            elif predicted_label == 0 and true_label == 1:
                self.false_negatives += 1
            elif predicted_label == 0 and true_label == 0:
                self.true_negatives += 1