from preprocess import preprocess_text
from collections import defaultdict
from similarity import calculate_cosine_similarity

def process_queries(queries, dictionary, inverted_index, documents):
    for query in queries:
        query_terms = set(preprocess_text(query))
        relevant_documents = set()

        for term in query_terms:
            if term in inverted_index:
                if not relevant_documents:
                    relevant_documents.update(inverted_index[term])
                else:
                    relevant_documents.intersection_update(inverted_index[term])

        print(f"Query: {query}")

        if not relevant_documents:
            print("No relevant documents found.")
            continue

        relevant_document_ids = [doc_id for doc_id in relevant_documents]

        print(f"Relevant documents: {' '.join(map(str, relevant_document_ids))}")

        query_vector = {term: 1 for term in query_terms if term in dictionary}
        results = []

        for doc_id in relevant_documents:
            doc_vector = defaultdict(int)
            terms = preprocess_text(documents[doc_id - 1])
            for term in terms:
                if term in dictionary:
                    doc_vector[term] += 1
            similarity_score = calculate_cosine_similarity(query_vector, doc_vector)
            results.append((doc_id, similarity_score))

        results.sort(key=lambda x: x[1], reverse=True)

        for doc_id, similarity_score in results:
            print(f"{doc_id} {similarity_score:.5f}")


# def process_queries(queries, dictionary, inverted_index, documents):
#     for query in queries:
#         query_terms = set(preprocess_text(query))
#         relevant_documents = set()

#         for term in query_terms:
#             if term in inverted_index:
#                 if not relevant_documents:
#                     relevant_documents.update(inverted_index[term])
#                 else:
#                     relevant_documents.intersection_update(inverted_index[term])

#         print(f"Query: {query}")

#         if not relevant_documents:
#             print("No relevant documents found.")
#             continue

#         relevant_document_ids = [doc_id for doc_id in relevant_documents]

#         print(f"Relevant documents: {' '.join(map(str, relevant_document_ids))}")

#         query_vector = {term: 1 for term in query_terms if term in dictionary}
#         results = []

#         for doc_id in relevant_documents:
#             doc_vector = defaultdict(int)
#             terms = preprocess_text(documents[doc_id - 1])
#             for term in terms:
#                 if term in inverted_index:
#                     doc_vector[term] += 1

#             if not doc_vector:
#                 similarity_score = 0.0
#             else:
#                 similarity_score = calculate_cosine_similarity(query_vector, doc_vector)
#             results.append((doc_id, similarity_score))

#         results.sort(key=lambda x: x[1], reverse=True)

#         for doc_id, similarity_score in results:
#             print(f"{doc_id} {similarity_score:.2f}")
