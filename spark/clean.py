def clean_data(data):
    cleaned = []
    for item in data:
        text = item["text"].replace("，", " ")
        cleaned.append({"id": item["id"], "text": text})
    return cleaned
