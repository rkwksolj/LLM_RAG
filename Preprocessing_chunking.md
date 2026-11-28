# Document Preprocessing and Chunking Pipeline
Raw documents often **contain complex layouts and formats, requiring preprocessing and chunking before embedding**.  

Raw documents(from Amazon S3) are **parsed, cleaned, chunked, embedded** into vectors, and stored in a vector **index for retrieval**.  

- **Parsing: Extract text** from raw documents.
- **Cleaning: Remove irrelevant content** and noise.
- **Chunking: Split text** into retrieval-friendly chunks.
- **Embedding: Convert chunks into vector representations**.
- **Indexing: Store vectors, text, and metadata** in a vector index.
- **Retrieval: Search and retrieve** the most relevant chunks.

Two approaches:  
A **custom LangChain pipeline provides full control over document parsing and chunking**, while **Amazon Bedrock Knowledge Bases automates the entire ingestion process** from parsing to indexing.  

- **Chunking involves decisions** on size, overlap, strategy, and metadata, with no one-size-fits-all solution. High-quality preprocessing and chunking are critical to RAG performance. Even the best models cannot compensate for poor data quality.


## PDF/text parsing  
Parsing extracts machine-readable text from documents. Since it is the **first step in the pipeline, poor parsing propagates to all downstream** stages and can impact retrieval quality.  
| Issue | Description | Impact |
|-------|-------------|--------|
| Multi-column Layout | Text from different columns becomes mixed | Context is corrupted |
| Headers & Footers | Page numbers and document titles are inserted into the content | Lower embedding quality |
| Tables | Row and column structure is flattened into plain text | Reduced data accuracy |
| Scanned PDFs | Text exists only as images and cannot be extracted directly | OCR required |
