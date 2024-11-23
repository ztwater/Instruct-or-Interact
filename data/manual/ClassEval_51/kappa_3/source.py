class KappaCalculator:
    def kappa(matrix):
        # Convert the matrix to a numpy array
        matrix = np.array(matrix)
        
        # Calculate the observed agreement
        observed_agreement = np.trace(matrix) / np.sum(matrix)
        
        # Calculate the expected agreement
        row_totals = np.sum(matrix, axis=0)
        column_totals = np.sum(matrix, axis=1)
        expected_agreement = np.sum(row_totals * column_totals) / np.sum(matrix)**2
        
        # Calculate the Cohen's kappa value
        kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
        
        return kappa_value