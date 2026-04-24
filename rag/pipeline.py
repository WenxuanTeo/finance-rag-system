import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
import faiss

# 1️⃣ 加载向量模型（轻量版）
model = SentenceTransformer('all-MiniLM-L6-v2')


# =========================
# 构建索引
# =========================
def build_index(chunks):
    corpus = [c["chunk"] for c in chunks]

    # BM25
    tokenized = [doc.split() for doc in corpus]
    bm25 = BM25Okapi(tokenized)

    # 向量
    embeddings = model.encode(corpus)
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    return bm25, index, corpus, embeddings


# =========================
# 检索（Hybrid）
# =========================
def search(query, bm25, index, corpus, chunks, embeddings, top_k=3):
    # BM25
    tokenized_query = query.split()
    bm25_scores = bm25.get_scores(tokenized_query)

    # 向量
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), top_k)

    vector_scores = np.zeros(len(corpus))
    for i, idx in enumerate(I[0]):
        vector_scores[idx] = 1 / (1 + D[0][i])  # 距离转分数

    # 融合（可调权重）
    final_scores = 0.5 * bm25_scores + 0.5 * vector_scores

    # 排序
    top_idx = np.argsort(final_scores)[::-1][:top_k]

    results = [(final_scores[i], chunks[i]) for i in top_idx]
    return results
