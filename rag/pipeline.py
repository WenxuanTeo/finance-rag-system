from rank_bm25 import BM25Okapi

def build_index(chunks):
    corpus = [c["chunk"].split() for c in chunks]
    bm25 = BM25Okapi(corpus)
    return bm25, corpus

def search(query, bm25, corpus, chunks):
    tokenized_query = query.split()
    scores = bm25.get_scores(tokenized_query)

    ranked = sorted(
        zip(scores, chunks),
        key=lambda x: x[0],
        reverse=True
    )

    return ranked[:2]  # top-k
