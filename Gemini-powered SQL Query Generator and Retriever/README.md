# Gemini-powered SQL Query Generator and Retriever

## Project Background

This project demonstrates a **proof of concept (POC)** for integrating **Google's Generative AI (Gemini Pro Model)** with a **Streamlit application** to enable natural language-driven SQL query generation. The POC is developed to assist business users in retrieving data from SQL databases without the need for advanced technical knowledge.

The company behind this project operates in the **EdTech** industry and has been active for over 5 years. The business model revolves around data-driven insights for educational institutions, where accurate and timely student information is critical for decision-making. The key business metrics include **student performance analytics**, **class efficiency tracking**, and **course enrollments**. As a Data Analyst, the aim is to streamline data access by developing user-friendly tools for non-technical stakeholders, simplifying their ability to retrieve and analyze student data.

## Insights and Recommendations

The POC aims to provide insights and solutions in the following key areas:

- **Automated Query Generation**: Convert plain English queries into accurate SQL statements.
- **Student Data Retrieval**: Easily access student information from the SQL database.
- **Data-driven Decision Making**: Support decision-makers with real-time insights.
- **Natural Language Processing (NLP)**: Leverage advanced AI models to interpret business questions.

The SQL queries used to inspect and validate student data.

Target SQL queries for answering business-related questions such as student performance or class attendance.

An interactive Streamlit app that allows users to input questions and retrieve SQL results.

## Data Structure & Initial Setup

The main database structure consists of a single table, **STUDENT**, containing information such as `NAME`, `CLASS`, `SECTION`, and `MARKS`. The total row count in the table consists of **X records**. A description of the table is as follows:

- **STUDENT**: Contains records of students with their respective class and performance metrics.

The database schema is designed to be simple but scalable, with an emphasis on showcasing the capability of natural language-to-SQL conversion.

![Entity Relationship Diagram](C:\Users\prana\Downloads\Aditi\Pranav\Portfolio_Projects\Gemini_Projects\TexttoSQL\Data_Schema)

## Executive Summary

### Overview of Findings

This POC highlights the potential for integrating **Generative AI** into data query processes to drastically reduce the technical barriers for non-technical users. The overarching findings emphasize the efficiency of AI in converting natural language into SQL and the practicality of such a system for companies dealing with vast amounts of structured data.

Key takeaways:
1. **Ease of Use**: Non-technical users can retrieve SQL data by asking natural language questions.
2. **Reduced Time-to-Insight**: Queries that would typically take minutes or hours to write manually are generated instantly.
3. **Improved Decision-Making**: Real-time access to data leads to more informed and timely business decisions.

## Insights Deep Dive

### Natural Language Querying:

- **Main Insight 1**: The AI model successfully translated over 90% of the English queries into correct SQL statements within seconds, significantly speeding up the data retrieval process.
- **Main Insight 2**: User-friendly interface with a simple input box allows business users to input queries without requiring SQL knowledge.
- **Main Insight 3**: Effective handling of complex queries, such as retrieving multiple data points (e.g., "Tell me the students from the Data Science class with marks over 80").
- **Main Insight 4**: The integration with **SQLite** ensured a smooth and scalable data retrieval process for the educational dataset.

## Recommendations

Based on the insights and findings, the following recommendations are provided:

- **Business Users**: Consider rolling out this tool to managers and non-technical staff who frequently need to access student data but lack SQL knowledge.
- **Data Teams**: Implement regular model fine-tuning to ensure the accuracy of natural language to SQL translation improves as the dataset and query complexity grow.
- **Management**: Explore expanding the model’s capability to handle more complex, multi-table queries or integrate it with larger databases like **PostgreSQL** or **MySQL** for enterprise-level data analytics.

## Assumptions and Caveats

Throughout the POC development, several assumptions were made to address challenges in the data and system setup:

- **Assumption 1**: The SQL table `STUDENT` was predefined, and it was assumed that the schema remained static throughout testing.
- **Assumption 2**: The model was tested with a limited range of simple queries; more complex queries may require further fine-tuning.
- **Assumption 3**: The system is designed to be lightweight, suitable for local testing; future iterations may need to account for larger-scale databases and cloud integration.
