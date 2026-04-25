from rag.rewrite import rewrite
from rag.retriever import hybrid_search
from rag.rerank import rerank


def run_pipeline(query, chunks, bm25, index, corpus, embeddings):
    new_query = rewrite(query)
    print("🔁 Rewrite:", new_query)

    idxs = hybrid_search(new_query, bm25, index, corpus, embeddings)

    candidates = [chunks[i] for i in idxs]

    results = rerank(new_query, candidates)

    return results[:3]
