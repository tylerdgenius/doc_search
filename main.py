from pathlib import Path
from indexing import build_dictionary_and_inverted_index
from query import process_queries

def main():
    # Need a way to confirm if files exists before I start readsing it
    docs_file_path = Path("docs.txt")
    queries_file_path = Path("queries.txt")

    if not docs_file_path.exists():
        print(f"Error: '{docs_file_path}' file not found. Please ensure the file exists.")
        return

    if not queries_file_path.exists():
        print(f"Error: '{queries_file_path}' file not found. Please ensure the file exists.")
        return
    
    with open(docs_file_path, "r") as docs_file:
        documents = [line.strip() for line in docs_file.readlines()]

    with open(queries_file_path, "r") as queries_file:
        queries = [line.strip() for line in queries_file.readlines()]

    dictionary, inverted_index = build_dictionary_and_inverted_index(documents)

    print(f"Words in dictionary: {len(dictionary)}")

    process_queries(queries, dictionary, inverted_index, documents)


