class KappaCalculator:
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the fleiss kappa value of an N * k matrix
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, fleiss kappa value
        """
        matrix = np.array(testData)
        p = np.sum(matrix * (matrix - 1), axis=1) / (n * (n - 1))
        P = np.sum(p) / N
        P_e = np.sum(np.square(np.sum(matrix, axis=0) / (N * n)))
        kappa = (P - P_e) / (1 - P_e)
        return kappa