def chunk_data(data):
    chunks = []
    for item in data:
        chunks.append({
            "id": item["id"],
            "chunk": item["text"]
        })
    return chunks
