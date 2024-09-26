# 📚 Chat with Multiple PDFs Using Gemini

## 💼 Project Background

The **Chat with Multiple PDFs Using Gemini** application enables users to upload multiple PDF files and interact with the content using natural language queries. This tool leverages **Google's Generative AI (Gemini)** model to process and retrieve relevant information from uploaded documents, offering a seamless way to extract insights from large text-based data sources.

This project is ideal for businesses, researchers, or professionals dealing with large sets of documents who need a quick and efficient way to extract answers to specific questions from multiple PDFs.

---

## 🎯 Key Features and Insights

This project focuses on:

- **Multi-PDF Support**: Upload multiple PDF files and process their content simultaneously.
- **AI-driven Question-Answering**: Ask questions related to the uploaded PDFs, and the AI model will retrieve relevant information.
- **Vector Store**: Store PDF content in vector form for efficient similarity search and fast query resolution.
- **Accurate Answering**: The system avoids guessing by only providing responses based on the actual content of the PDFs.

---

## 🗃️ Data Structure & System Overview

This project relies on the following key components:

1. **PDF Extraction**: Extracts text from the uploaded PDFs using the `PyPDF2` library.
2. **Text Chunking**: Breaks down large text documents into manageable chunks using the `RecursiveCharacterTextSplitter`.
3. **Google Generative AI Embeddings**: Converts chunks of text into vector embeddings, which are stored locally using **FAISS**.
4. **Generative AI Model**: A conversational chain powered by **Gemini** is used to generate accurate responses based on the similarity search results.

---

## 🚀 Executive Summary

### 📌 Key Findings:

- The application provides an easy and efficient way to extract information from large amounts of PDF data.
- Users can query the PDF content with natural language and receive relevant answers based on the actual document content.
- Text data is stored in a vector format, allowing for fast and accurate information retrieval.

---

## 🔍 Insights Deep Dive

### 🧠 Main Insights:

- **Multi-PDF Processing**: The ability to upload and process multiple PDFs at once makes it highly efficient for users managing large document sets.
- **AI-driven QA System**: The AI model (Gemini) generates highly accurate answers based on context within the documents, avoiding out-of-context responses.
- **Vectorized Search**: The **FAISS** vector store allows the system to perform quick similarity searches on the documents, ensuring fast response times for complex queries.
- **Robust Text Processing**: The use of `RecursiveCharacterTextSplitter` ensures that large chunks of text are divided and processed effectively, maintaining coherence in responses.

---

## 🛠️ Recommendations

- **For Researchers**: Use this tool to quickly find relevant information within academic papers or reports without manually going through each document.
- **For Legal Professionals**: This tool can speed up the document review process by extracting relevant details from legal contracts, agreements, or case studies.
- **For Business Analysts**: Analyze financial or technical reports to get precise answers to specific business questions.

---

## 📂 Project Structure

### Main Components:
1. **PyPDF2**: Extracts text from uploaded PDF files.
2. **Langchain Text Splitter**: Splits large texts into smaller, coherent chunks.
3. **Google Generative AI (Gemini)**: Powers the conversational model to provide detailed answers.
4. **FAISS Vector Store**: Stores text embeddings and retrieves documents based on similarity searches.

### Data Flow:
1. **PDF Upload**: User uploads PDF files.
2. **Text Extraction**: Extracted text is split into chunks.
3. **Vector Embeddings**: Text chunks are converted to embeddings and stored locally.
4. **Querying**: User asks a question, and the system retrieves relevant content from the vector store, generating an answer via the AI model.

---

## ⚠️ Assumptions and Caveats

The following assumptions were made during the development of this project:

- **Assumption 1**: The uploaded PDFs are text-based (not scanned images).
- **Assumption 2**: The PDF text content is in a format that the language model can process effectively.
- **Assumption 3**: The embeddings created by the **Gemini model** are stored securely in the local environment.

---

## 📂 Project Links

---

## 💡 How to Run the Project

1. Clone the repository.
2. Install the required dependencies using:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up your **Google Generative AI** API Key in your `.env` file.
4. Run the application using:
    ```bash
    streamlit run app.py
    ```
5. Upload PDF files and ask questions to interact with the PDF content.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
