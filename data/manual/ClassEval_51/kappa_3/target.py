class KappaCalculator:
    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return: float, the cohens kappa value of the matrix
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
        # Convert the matrix to a numpy array
        matrix = np.array(testData)
        
        # Calculate the observed agreement
        observed_agreement = np.trace(matrix) / np.sum(matrix)
        
        # Calculate the expected agreement
        row_totals = np.sum(matrix, axis=0)
        column_totals = np.sum(matrix, axis=1)
        expected_agreement = np.sum(row_totals * column_totals) / np.sum(matrix)**2
        
        # Calculate the Cohen's kappa value
        kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
        
        return kappa_value