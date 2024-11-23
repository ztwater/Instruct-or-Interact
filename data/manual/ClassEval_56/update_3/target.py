class MetricsCalculator:
    def update(self, predicted_labels, true_labels):
        """
        Update the number of all four samples(true_positives, false_positives, false_negatives, true_negatives)
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: None, change the number of corresponding samples
        """
        for predicted, true in zip(predicted_labels, true_labels):
            # Update the number of true positives
            if predicted == 1 and true == 1:
                self.true_positives += 1
        
            # Update the number of false positives
            if predicted == 1 and true == 0:
                self.false_positives += 1
        
            # Update the number of false negatives
            if predicted == 0 and true == 1:
                self.false_negatives += 1
        
            # Update the number of true negatives
            if predicted == 0 and true == 0:
                self.true_negatives += 1