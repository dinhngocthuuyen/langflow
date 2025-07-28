## 📦 Quickstart
```shell
cd docker
docker compose -f dev.docker-compose.yml up
```

Default Username: postgres <br/>
Default Password: 1

## Introduction
Langflow is a visual IDE for quickly building powerful RAG and multi-agent AI applications with advanced agentic pipelines. Easily add, swap, and compare models or AI services using intuitive settings—no need to master complex APIs or frameworks. <br/>
Key Features: <br/>
•	Visual Flow Builder: Langflow provides a drag-and-drop interface, enabling developers to construct complex AI workflows without extensive coding. This visual approach allows for seamless connection of components such as prompts, language models, and data sources. <br/>
•	Model Integration Support: The platform supports leading AI models, allowing users to tailor workflows to leverage the strengths of different models for diverse applications.  <br/>
•	Python-Based and Agnostic: Langflow is built on Python and is agnostic to models, APIs, data sources, or databases, providing flexibility in integrating various technologies.  <br/>
•	Playground for Testing: A built-in playground enables immediate testing and iteration of workflows, offering step-by-step control to refine AI applications effectively.  <br/>
•	Multi-Agent Orchestration: Langflow facilitates the management of multiple agents, allowing for sophisticated conversation handling and retrieval mechanisms within AI applications.  <br/>
•	API Key Functionality: The platform offers API key support, enabling users to access individual components and flows without traditional login authentication, thus simplifying integration and enhancing security.  <br/>

## Demonstration
With a user-friendly drag-and-drop interface, users can efficiently upload and process data with minimal effort. Here an example for RAG:
 <img width="468" alt="image" src="https://github.com/user-attachments/assets/3e72a358-c7a4-4e8c-ae8f-9b4885e84201" />

**The Ingestion Flow** loads data from a local file and external URLs then embed it into the vector database.  <br/>
It ingests data from a file (**File Component**) and a list of URLs (**URL component**).  <br/>
-	File Component: a class that loads and parses text files of various supported formats, converting the content into a Data object. The files are save in config folder “/var/lib/langflow”.
-	URL Component: a class that fetches content from one or more URLs, processes the content, and returns it as a list of Data objects. It ensures that the provided URLs are valid and uses WebBaseLoader to fetch the content.

**Split Text Component**: splits the incoming Data into chunks to be embedded into the vector store component.  <br/>
Indexes it in Postgres DB by **PGVector Component**.  **Storage of Vector Embeddings**: After data is processed and split into manageable chunks, the CloudCIX Embeddings Component computes vector embeddings for each chunk. These embeddings are numerical representations that capture the semantic essence of the data. The PGVector component stores these embeddings within a PostgreSQL database, allowing for efficient organization and retrieval.

**CloudCIX Embeddings Component**: Computes embeddings for the chunks using an embedding model.  <br/>
 	
 <img width="468" alt="image" src="https://github.com/user-attachments/assets/be6dbffa-adce-4f8c-ba4e-758375d8dfec" />

**The Retriever Flow** answers the questions with contextual data retrieved from the vector database. The vector data from Ingestion flow can then be retrieved for workloads.  <br/>

**Chat Input Component** defines where to send the user input (coming from the Playground). <br/>

**Memory History Component** plays a crucial role in maintaining conversational context by storing and retrieving chat messages. This functionality ensures that interactions with AI models are coherent and contextually relevant. **Storage**: When a user sends a message through the Chat Input component, the message can be configured to be stored in the chat history. The stored messages are saved as Data objects, preserving essential details such as the message content, sender information, and session ID. **Retrieval**: The Message History component is responsible for fetching these stored messages. It retrieves the chat history associated with a specific session ID, providing the sequence of previous interactions. This historical data can then be fed into the Prompt component, allowing the AI model to generate responses that consider the prior context of the conversation.

**CloudCIX Embeddings Component** is the model used to generate embeddings from the user input.  <br/>

**PGVector Component** creates a PGVector Vector Store with search capabilities, receives the query embedding and compares it with stored data to retrieve the most contextually relevant matches. **Facilitating Similarity Searches**: When a user query is received, it is transformed into a vector embedding using the same embedding model. The PGVector component then performs a similarity search between this query embedding and the stored embeddings in the database. By calculating the proximity between vectors, PGVector identifies and retrieves data chunks that are most relevant to the user's query. <br/>

**Data To Message Component** converts chunks coming from the DB component into plain text to feed a prompt. <br/>

**Prompt Component** takes in the user input and the retrieved chunks as text and builds a prompt for the model. <br/>

**CloudCIX Component** takes in the prompt to generate a response. <br/>

**Chat Output Component** displays the response in the Playground. <br/>

## API/Chat Widget HTML Integration
Guide on integrating an API/Chat widget HTML into a website. <br/>
Information on UI customization, user authentication, message/conversation saving, and data storage methods. <br/>
 
Message Storage Flow:  <br/>
a.	When a user sends a message, a Message object is called including various attributes such as text, sender, sender_name, session_id, timestamp, flow_id, and a unique id <br/>
b.	To retrieve messages, the system queries the storage based on parameters: flow_id, session_id, sender, or sender_name <br/>
c.	Once the query is executed, the resulting messages are transformed into MessageResponse objects. <br/>
