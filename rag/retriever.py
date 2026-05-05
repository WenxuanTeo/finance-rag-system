from langchain.vectorstores import FAISS

vectorstore = None

def build_retriever(chunks, embedder):
    global vectorstore
    texts = [c["chunk"] for c in chunks]
    vectorstore = FAISS.from_texts(texts, embedder)


def retrieve(query, k=5):
    return vectorstore.similarity_search(query, k=k)
