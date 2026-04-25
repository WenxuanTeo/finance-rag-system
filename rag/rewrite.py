from transformers import pipeline

rewriter = pipeline("text2text-generation", model="google/flan-t5-base")

def rewrite(query):
    prompt = f"Rewrite for search: {query}"
    return rewriter(prompt, max_length=64)[0]["generated_text"]
