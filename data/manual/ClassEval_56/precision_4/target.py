class MetricsCalculator:
    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        self.true_positives = 0
        self.false_positives = 0
    
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                self.true_positives += 1
            elif predicted == 1 and true == 0:
                self.false_positives += 1
    
        if self.true_positives + self.false_positives == 0:
            return 0
        else:
            return self.true_positives / (self.true_positives + self.false_positives)