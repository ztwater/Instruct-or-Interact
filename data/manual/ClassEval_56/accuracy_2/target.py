class MetricsCalculator:
    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        correct = 0
        total = len(predicted_labels)

        for pred, label in zip(predicted_labels, true_labels):
            if pred == label:
                correct += 1

        accuracy = correct / total
        return accuracy
