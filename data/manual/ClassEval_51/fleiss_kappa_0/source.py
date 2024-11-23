class KappaCalculator:
    def fleiss_kappa(matrix):
        N, k = matrix.shape
        n = np.sum(matrix, axis=1)
        p = np.sum(matrix * (matrix - 1), axis=1) / (n * (n - 1))
        P = np.sum(p) / N
        P_e = np.sum(np.square(np.sum(matrix, axis=0) / (N * n)))
        kappa = (P - P_e) / (1 - P_e)
        return kappa