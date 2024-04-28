import math

def calculate_cosine_similarity(query_vector, doc_vector):
    dot_product = sum(query_vector[word] * doc_vector[word] for word in query_vector if word in doc_vector)
    query_norm = math.sqrt(sum(query_vector[word]**2 for word in query_vector))
    doc_norm = math.sqrt(sum(doc_vector[word]**2 for word in doc_vector))
    
    if query_norm == 0 or doc_norm == 0:
        return 0.0
    
    cosine_similarity = dot_product / (query_norm * doc_norm)
    angle_in_degrees = math.degrees(math.acos(cosine_similarity))
    return angle_in_degrees