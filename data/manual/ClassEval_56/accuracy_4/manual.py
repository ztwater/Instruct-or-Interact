### Method Description:
    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>>mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """

### Solution Code:
    def accuracy(self, predicted_labels, true_labels):
        self.update(predicted_labels, true_labels)
        total = self.true_positives + self.true_negatives + self.false_positives + self.false_negatives
        if total == 0:
            return 0.0
        return (self.true_positives + self.true_negatives) / total

### Source Code:
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

### Predicted Code:
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


### Adaptation:
Total number: 9
### Raw Output:
```
class MetricsCalculator:  
    """
    The class calculates precision, recall, F1 score, and accuracy based on predicted and true labels.
    """

    def __init__(self):
        """
        Initialize the number of all four samples to 0
        """
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0

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

    def update(self, predicted_labels, true_labels):
        pass

    def precision(self, predicted_labels, true_labels):
        pass

    def recall(self, predicted_labels, true_labels):
        pass

    def f1_score(self, predicted_labels, true_labels):
        pass

```

### Test Code:
class MetricsCalculatorTestAccuracy(unittest.TestCase):
    def test_accuracy_1(self):
        mc = MetricsCalculator()
        temp = mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
        self.assertEqual(temp, 0.5)

    def test_accuracy_2(self):
        mc = MetricsCalculator()
        temp = mc.accuracy([1, 1, 2, 0], [1, 0, 0, 1])
        self.assertAlmostEqual(temp, 0.3333333333333333)

    def test_accuracy_3(self):
        mc = MetricsCalculator()
        temp = mc.accuracy([1, 1, 0, 1], [1, 0, 0, 1])
        self.assertEqual(temp, 0.75)

    def test_accuracy_4(self):
        mc = MetricsCalculator()
        temp = mc.accuracy([1, 1, 0, 0], [1, 1, 0, 1])
        self.assertEqual(temp, 0.75)

    def test_accuracy_5(self):
        mc = MetricsCalculator()
        temp = mc.accuracy([1, 1, 0, 0], [1, 0, 1, 1])
        self.assertEqual(temp, 0.25)

    def test_accuracy_6(self):
        mc = MetricsCalculator()
        temp = mc.accuracy([], [])
        self.assertEqual(temp, 0.0)

### Test Output:
# 1 errors, 1 failures in 6 runs.
# errors:
#     ZeroDivisionError:
#         test_accuracy_6: division by zero
# failures:
#     AssertionError:
#         test_accuracy_2: 0.25 != 0.3333333333333333 within 7 places (0.08333333333333331 difference)


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.false_negatives, self.false_positives, self.true_negatives, self.true_positives
# method_dependencies: update


