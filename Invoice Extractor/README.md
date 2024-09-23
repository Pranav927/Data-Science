# 🧾 Multi-language Invoice Extractor

## 💼 Project Background

The **Multi-language Invoice Extractor** is a proof of concept (POC) that integrates **Google's Gemini Pro Model** and **Streamlit** to create an application capable of extracting and interpreting data from uploaded invoice images. This tool is designed for businesses operating in multiple countries where invoices are generated in various languages. 

The application leverages **Generative AI** to understand invoice details and respond to user queries based on the uploaded image, streamlining the process of invoice analysis for accounting, compliance, or auditing teams.

---

## 🎯 Insights and Key Features

This project covers the following areas:

- **Invoice Data Extraction**: Extract relevant details from invoices uploaded as images or PDFs.
- **AI-driven Query Response**: Users can input natural language queries to get information based on the uploaded invoice.
- **Multi-language Support**: Capable of handling invoices in various languages through the use of AI models.
- **User-friendly Interface**: Simple, intuitive interface powered by **Streamlit**, allowing easy interaction for non-technical users.

---

## 🗃️ Data Structure & System Setup

The system relies on the following components:

- **Gemini Pro Model**: AI model for generating content and responding to queries.
- **Streamlit UI**: User interface for uploading invoices and entering queries.
- **Image/PDF Uploader**: Allows users to upload invoice images in formats like `.jpg`, `.jpeg`, and `.png`.

---

## 🚀 Executive Summary

### 📌 Key Findings:

- The **Multi-language Invoice Extractor** simplifies invoice management by allowing users to upload images or PDFs of invoices and get AI-powered responses to queries.
- Supports **multi-language invoices**, making it a versatile tool for global businesses.
- The tool significantly reduces manual effort by providing quick, accurate invoice details based on user input.

---

## 🔍 Insights Deep Dive

### 🧠 Main Insights:

- **Automated Invoice Processing**: With a few clicks, users can upload an invoice and receive structured responses.
- **AI Model Efficiency**: The **Gemini Pro model** accurately interprets invoice content and responds to queries with minimal input from the user.
- **Multi-language Flexibility**: The tool's ability to handle various languages makes it suitable for international businesses.
- **Real-time Response**: Query responses are generated instantly, reducing time spent on manual invoice review.

---

## 🛠️ Recommendations

Based on the insights gained from this project, the following recommendations can be made:

- **Accounting Teams**: Deploy the tool to streamline invoice review and querying, especially in multi-language environments.
- **Compliance Departments**: Use the tool to validate invoice content quickly without needing language expertise.
- **IT and Development Teams**: Expand the functionality by integrating additional AI models to handle even more complex invoice formats.

---

## 📂 Project Structure

### Main Components:
1. **Google Generative AI (Gemini Pro)**: For natural language understanding and query generation.
2. **Streamlit UI**: Front-end for uploading invoices and displaying responses.
3. **Pillow Library (PIL)**: Used to handle image uploads.

### Data Flow:
1. **Invoice Upload**: User uploads an invoice image or PDF.
2. **Prompt & Query Input**: User asks questions about the invoice.
3. **AI Model**: The Gemini Pro model processes the image and query to generate a response.
4. **Response Display**: The output is shown on the Streamlit UI.

---

## ⚠️ Assumptions and Caveats

The following assumptions were made during the development of this project:

- **Assumption 1**: The uploaded invoices are in a format that the AI model can interpret effectively.
- **Assumption 2**: The language of the invoice is supported by the Gemini model.
- **Assumption 3**: The AI response is based on the quality and clarity of the uploaded invoice image.

---

## 💡 How to Run the Project

1. Clone the repository.
2. Install the necessary packages by running:
    ```bash
    pip install -r requirements.txt
    ```
3. Ensure that your Google Generative AI API Key is set up in your `.env` file.
4. Run the Streamlit app using:
    ```bash
    streamlit run app.py
    ```
5. Upload an invoice image or PDF, and enter your query to get started!
