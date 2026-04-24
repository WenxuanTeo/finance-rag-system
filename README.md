# Financial Data Pipeline for RAG (Spark + Hybrid Retrieval)
A scalable financial data-centric RAG system with distributed processing (Apache Spark), hybrid search, reranking, and evaluation-driven optimization.

## Project Overview

This project builds a scalable financial data pipeline using Apache Spark to support RAG systems and large language model applications.

It focuses on:

- Processing large-scale financial documents (PDF / News / Reports)
- Data cleaning and structuring
- Hybrid retrieval (BM25 + Vector)
- Rerank optimization
- Evaluation-driven improvement

The goal is to improve RAG performance through better data and retrieval.

## System Architecture

Raw Data (PDF / Web / News)
↓
Spark Data Pipeline
↓
Cleaning & Structuring
↓
Chunking + Metadata
↓
Embedding
↓
Hybrid Retrieval (BM25 + Vector)
↓
Rerank
↓
LLM Generation
↓
Evaluation & Feedback#

# Key Features

- Distributed data processing (Spark)
- Financial document parsing (PDF / Web)
- Hybrid retrieval (BM25 + Vector)
- Cross-encoder reranking
- Evaluation metrics (Hit Rate / Accuracy)
- Modular pipeline design

## Project Structure

finance-data-pipeline-rag/
├── spark/
│   ├── spark_job.py
│   ├── ingest.py
│   ├── clean.py
│   ├── chunk.py
├── rag/
│   ├── pipeline.py
│   ├── retriever/
│   ├── rerank/
├── evaluation/
│   └── metrics.py
├── requirements.txt
└── README.md

## How to Run

### Install dependencies

pip install -r requirements.txt

### Run Spark pipeline

spark-submit spark/spark_job.py

### Run RAG pipeline

python rag/pipeline.py

## Example

Query: What is Tesla revenue growth?

Answer:
Tesla reported significant revenue growth driven by increased deliveries and global expansion...

## Evaluation

### Retrieval Metrics

- Hit Rate @K
- Recall @K

### Generation Metrics

- Answer Accuracy
- Groundedness
- Hallucination Rate

### Optimization Strategy

- Improve chunking
- Improve query rewrite
- Filter low-quality documents

## Future Improvements

- Knowledge graph integration
- Multi-hop QA dataset construction
- SFT data generation
- Streaming pipeline (Kafka + Spark)
