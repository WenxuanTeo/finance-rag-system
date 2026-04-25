from sentence_transformers import CrossEncoder

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank(query, candidates):
    pairs = [(query, c["chunk"]) for c in candidates]
    scores = reranker.predict(pairs)

    results = list(zip(scores, candidates))
    results.sort(key=lambda x: x[0], reverse=True)
    return results
