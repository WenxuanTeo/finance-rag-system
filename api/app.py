from fastapi import FastAPI
from rag.pipeline import run_pipeline

app = FastAPI()

@app.get("/query")
def query(q: str):
    return {"msg": "接口已启动"}
