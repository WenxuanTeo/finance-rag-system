# Financial RAG System (Spark + Hybrid Retrieval)

A scalable financial data-centric RAG system with distributed processing (Apache Spark), hybrid retrieval, reranking, and evaluation.

---

##  Project Overview

This project builds an end-to-end financial RAG system, focusing on improving retrieval quality and reducing hallucination in LLM applications.

Key capabilities:

- Financial document processing (PDF / News / Reports)
- Distributed data pipeline (Apache Spark)
- Hybrid retrieval (BM25 + Vector search)
- Query Rewrite for better recall
- Cross-encoder Rerank for precision
- Evaluation-driven optimization

---

##  My Contributions

- Designed **Spark-based data pipeline** for financial text processing
- Implemented **Hybrid Retrieval (BM25 + FAISS)** to improve recall
- Built **Query Rewrite module** to enhance search quality
- Integrated **Cross-Encoder Rerank** to improve ranking accuracy
- Developed **evaluation metrics (Hit Rate / Accuracy)** for iterative optimization
- Built **end-to-end pipeline** from data → retrieval → generation → evaluation

---

##  System Architecture

Raw Data → Spark Pipeline → Cleaning → Chunking → Embedding  
→ Hybrid Retrieval → Rerank → LLM → Evaluation

---

##  Project Structure
finance-rag-system/
├── spark/
├── rag/
├── evaluation/
├── api/
├── requirements.txt
└── README.md

---

##  How to Run

### 1️⃣ Install
pip install -r requirements.txt
### 2️⃣ Run pipeline
python -m spark.job
### 3️⃣ Start API
uvicorn api.app:app --reload

---

## 📊 Evaluation

### Retrieval

- Hit Rate @K
- Recall @K

### Generation

- Accuracy
- Groundedness

---

##  Key Highlights

- Combines **data engineering + LLM system design**
- Improves RAG quality via **Hybrid + Rewrite + Rerank**
- Fully **modular and production-oriented**

---

##  Future Work

- Knowledge Graph integration
- Multi-hop QA dataset generation
- Streaming pipeline (Kafka + Spark)
