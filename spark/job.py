from spark.ingest import load_data
from spark.clean import clean_data
from spark.chunk import chunk_data

from rag.retriever import build_retriever
from rag.pipeline import run_pipeline


def main():
    data = load_data()
    data = clean_data(data)
    chunks = chunk_data(data)

    bm25, index, corpus, embeddings = build_retriever(chunks)

    query = "利好政策"
    results = run_pipeline(query, chunks, bm25, index, corpus, embeddings)

    print("\n🔍 最终结果：")
    for score, item in results:
        print(score, item)


if __name__ == "__main__":
    main()
