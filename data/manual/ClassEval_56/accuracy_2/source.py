class MetricsCalculator:
    def accuracy(predictions, labels):
        """
        Calculate accuracy of model predictions.
    
        Args:
            predictions (list): List of predicted labels.
            labels (list): List of true labels.
    
        Returns:
            float: Accuracy of the model predictions.
        """
        correct = 0
        total = len(predictions)
    
        for pred, label in zip(predictions, labels):
            if pred == label:
                correct += 1
    
        accuracy = correct / total
        return accuracy