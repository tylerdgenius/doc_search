from collections import defaultdict
from preprocess import preprocess_text

def build_dictionary_and_inverted_index(documents):
    inverted_index = defaultdict(list)
    # At this point, values are empty so I want to come back here to create a set to insert here
    dictionary = set()

    for doc_id, doc_text in enumerate(documents, start=1):
        terms = preprocess_text(doc_text)
        unique_terms = set(terms)
        dictionary.update(unique_terms)

        for term in unique_terms:
            inverted_index[term].append(doc_id)

    return dictionary, inverted_index