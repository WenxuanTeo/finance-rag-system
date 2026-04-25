def chunk_data(data):
    return [{"id": d["id"], "chunk": d["text"]} for d in data]
