from ingest import load_data
from clean import clean_data
from chunk import chunk_data

from rag.pipeline import build_index, search
from evaluation.metrics import hit_rate


def main():
    # 1. 数据加载
    data = load_data()

    # 2. 清洗
    data = clean_data(data)

    # 3. chunk
    chunks = chunk_data(data)

    # 4. 建索引
    bm25, corpus = build_index(chunks)

    # 5. 查询
    query = "股市 利好"
    results = search(query, bm25, corpus, chunks)

    print("🔍 检索结果：")
    for score, item in results:
        print(score, item)

    # 6. 评估
    hr = hit_rate(results, "股市")
    print("📊 Hit Rate:", hr)


if __name__ == "__main__":
    main()
