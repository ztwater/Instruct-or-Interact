class Statistics3:
    def correlation_matrix(data):
        matrix = np.corrcoef(data)
        return matrix.tolist()

