# RAG Chatbot with AWS Bedrock and LangChain

This repository contains the implementation of a chatbot with Retrieval-Augmented Generation (RAG) capabilities. The chatbot leverages AWS Bedrock and LangChain to provide enhanced interactions by integrating retrieval-augmented generation.

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [Technologies Utilized](#technologies-utilized)
- [Running the Application](#running-the-application)

## Introduction

In this project, we aim to demonstrate the capabilities of Retrieval-Augmented Generation (RAG) by building a chatbot that leverages AWS Bedrock and LangChain. This chatbot integrates document retrieval and generation to provide contextually accurate and relevant responses.

## Key Features

- **Streamlit Interface**: A sleek and intuitive front-end interface for effortless interaction with the chatbot.
- **Context Awareness**: Maintains conversation context using LangChain's `ConversationBufferWindowMemory`.
- **Retrieval-Augmented Generation**: Enhances chatbot responses by integrating document retrieval with the `ConversationalRetrievalChain`.
- **Embeddings and Vector Store**: Utilizes AWS Bedrock embeddings and FAISS for in-memory vector storage.
- **PDF Document Source**: Uses a PDF document as a source for retrieval-augmented generation.

## Technologies Utilized

- **Streamlit**: For the front-end interface.
- **LangChain**: For managing conversation memory and retrieval chains.
- **AWS Bedrock**: For embeddings and pre-trained models.
- **FAISS**: As an in-memory vector store.
- **RecursiveCharacterTextSplitter**: For handling large text documents.
- **PyPDFLoader**: For loading PDF documents.

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Ensure you have your AWS credentials set up for accessing AWS Bedrock services.

## Running the Application

3. Start the Streamlit application:

    ```bash
    streamlit run rag_chatbot_app.py --server.port 8080
    ```

4. Open your web browser and navigate to the URL provided by Streamlit to interact with the chatbot.
