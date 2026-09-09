# RAG Playground

Exploring how raw documents turn into useful knowledge — from ingestion and chunking to embeddings, retrieval, and LLM-powered answers.

This repository contains my RAG experiments, examples, and projects as I learn and build with Retrieval-Augmented Generation.

## What is RAG?

Retrieval-Augmented Generation (RAG) combines information retrieval with Large Language Models (LLMs).

Instead of asking an LLM to answer only from what it learned during training, RAG allows it to retrieve relevant information from an external knowledge base and use that information to generate an answer.

The basic flow looks like this:

```text
Documents
    ↓
Document Loading
    ↓
Text Splitting
    ↓
Embeddings
    ↓
Vector Database
    ↓
Retriever
    ↓
Relevant Context
    ↓
LLM
    ↓
Answer
