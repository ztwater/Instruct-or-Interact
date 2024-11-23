class VectorUtil:
    def cosine_similarities(vector, other_vectors):
        similarities = []
        for other_vector in other_vectors:
            dot_product = np.dot(vector, other_vector)
            norm_vector = np.linalg.norm(vector)
            norm_other_vector = np.linalg.norm(other_vector)
            similarity = dot_product / (norm_vector * norm_other_vector)
            similarities.append(similarity)
        return similarities