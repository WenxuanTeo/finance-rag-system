import numpy as np
from rank_bm25 import BM25Okapi
import faiss
from rag.embedder import encode


def build_retriever(chunks):
    corpus = [c["chunk"] for c in chunks]

    tokenized = [doc.split() for doc in corpus]
    bm25 = BM25Okapi(tokenized)

    embeddings = encode(corpus)
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    return bm25, index, corpus, embeddings


def hybrid_search(query, bm25, index, corpus, embeddings, top_k=5):
    tokenized_query = query.split()
    bm25_scores = bm25.get_scores(tokenized_query)

    query_vec = encode([query])
    D, I = index.search(query_vec, top_k * 3)

    vector_scores = np.zeros(len(corpus))
    for i, idx in enumerate(I[0]):
        vector_scores[idx] = 1 / (1 + D[0][i])

    final = 0.5 * bm25_scores + 0.5 * vector_scores
    top_idx = np.argsort(final)[::-1][:top_k * 3]

    return top_idx
