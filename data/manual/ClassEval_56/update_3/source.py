class MetricsCalculator:
    def update(true_positives, false_positives, false_negatives, true_negatives):
        # Update the number of true positives
        true_positives += 1
    
        # Update the number of false positives
        false_positives += 1
    
        # Update the number of false negatives
        false_negatives += 1
    
        # Update the number of true negatives
        true_negatives += 1
    
        return true_positives, false_positives, false_negatives, true_negatives