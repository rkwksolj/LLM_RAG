# Fundamental of RAG:  
(Simply put,)  
**1. Embedding Model -> Convert text into embeddings (vectors)**  
**2. Vector Database -> Retrieve relevant documents**  
**3. LLM -> Generate a response**  

In other words,
User question
-> **Embedding model** generates a vector for the query  
-> **Vector database** retrieves relevant documents  
-> Retrieved documents are combined with the query  
-> The augmented prompt is sent to the LLM  
-> **LLM generates** a response

<img width="508" height="283" alt="image" src="https://github.com/user-attachments/assets/e4348194-020d-48f8-a5e3-2d84b80e4901" />  
(https://truera.com/ai-quality-education/generative-ai-rags/what-is-retrieval-augmented-generation-rag-for-llms/)  

  
## Embedding  
The process of converting **data(especially text) into numerical vector** representations ***in vector space.***  
- **cosine similarity**: measure **semantic similarity** between embeddings based on the angle between their vectors.  
- **semantic search**: The process of finding information based on meaning rather than exact keyword matches. We used *embeddings and cosine similarity* to retrieve the most semantically relevant documents.

***NOTE: Different embedding models produce different vector representations for the same text.***  
<img width="500" height="220" alt="image" src="https://github.com/user-attachments/assets/eae5bb1f-85f3-415c-9196-a23877fbe1be" />  




##

