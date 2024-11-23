class MetricsCalculator2:
    def map(input_data):
        # Compute the Average Precision (AP) for each data point
        ap_list = []
        for data_point in input_data:
            # Compute the precision and recall for the data point
            precision = compute_precision(data_point)
            recall = compute_recall(data_point)
            
            # Compute the Average Precision (AP) for the data point
            ap = precision * recall
            
            # Add the AP to the list of APs
            ap_list.append(ap)
        
        # Compute the Mean Average Precision (MAP) by taking the mean of APs
        map_score = sum(ap_list) / len(ap_list)
        
        return map_score