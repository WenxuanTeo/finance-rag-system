from rag.rewrite import rewrite
from rag.retriever import retrieve
from rag.rerank import rerank


def run_pipeline(query):
    # 1. rewrite
    new_query = rewrite(query)

    # 2. retrieve
    docs = retrieve(new_query)

    # ❗ fallback
    if not docs:
        return "No relevant information found."

    # 3. rerank
    docs = rerank(new_query, docs)

    # 4. 控制top-k
    top_docs = docs[:3]

    # 5. build context
    context = "\n".join([d.page_content for d in top_docs])

    # 6. prompt
    prompt = f"""
Answer based on context only.

Context:
{context}

Question:
{query}
"""

    return call_llm(prompt)
