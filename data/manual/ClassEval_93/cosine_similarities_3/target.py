class VectorUtil:
    def cosine_similarities(vector_1, vectors_all):
        """
        Compute cosine similarities between one vector and a set of other vectors.
        :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :param vectors_all: list of numpy.ndarray, For each row in vectors_all, distance from vector_1 is computed, expected shape (num_vectors, dim).
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and each row in `vectors_all`, shape (num_vectors,).
        >>> vector1 = np.array([1, 2, 3])
        >>> vectors_all = [np.array([4, 5, 6]), np.array([7, 8, 9])]
        >>> VectorUtil.cosine_similarities(vector1, vectors_all)
        [0.97463185 0.95941195]
        """
        similarities = []
        for other_vector in vectors_all:
            dot_product = np.dot(vector_1, other_vector)
            norm_vector = np.linalg.norm(vector_1)
            norm_other_vector = np.linalg.norm(other_vector)
            similarity = dot_product / (norm_vector * norm_other_vector)
            similarities.append(similarity)
        return similarities