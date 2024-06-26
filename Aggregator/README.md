- **Project Overview**: A chatbot application using LangChain and OpenAI to solve logic-based and numeric questions, integrating Wikipedia API for additional information retrieval.
- **Key Features**: Utilizes OpenAI's GPT-3.5-turbo-instruct model for logic and reasoning; employs a math chain for numeric calculations with a dedicated calculator tool; uses Wikipedia API to fetch information on various topics.
- **Main Components**: Custom prompt templates for generating responses; three primary tools - Reasoning Tool, Calculator, and Wikipedia Tool; agent setup with LangChain's zero-shot react description for dynamic question answering.
- **Workflow**: Initializes the agent and tools on chat start; asynchronously processes user queries and generates responses using the initialized agent.
- **Environment Setup**: Uses `dotenv` to load environment variables for configuration.
