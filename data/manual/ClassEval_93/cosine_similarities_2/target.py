class VectorUtil:
    def cosine_similarities(vector_1, vectors_all):
        similarities = []
        for other_vector in vectors_all:
            dot_product = np.dot(vector_1, other_vector)
            norm_vector_1 = np.linalg.norm(vector_1)
            norm_other_vector = np.linalg.norm(other_vector)
            similarity = dot_product / (norm_vector_1 * norm_other_vector)
            similarities.append(similarity)
        return similarities