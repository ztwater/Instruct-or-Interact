class MetricsCalculator:
    def update(self, predicted_labels, true_labels):
        """
        Update the number of all four samples(true_positives, false_positives, false_negatives, true_negatives)
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: None, change the number of corresponding samples
        >>> mc = MetricsCalculator()
        >>> mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        (self.true_positives, self.false_positives, self.false_negatives, self.true_negatives) = (1, 1, 1, 1)
        """
        # Update the number of true positives
        self.true_positives += predicted_labels.count(1) * true_labels.count(1)
    
        # Update the number of false positives
        self.false_positives += predicted_labels.count(1) * true_labels.count(0)
    
        # Update the number of false negatives
        self.false_negatives += predicted_labels.count(0) * true_labels.count(1)
    
        # Update the number of true negatives
        self.true_negatives += predicted_labels.count(0) * true_labels.count(0)