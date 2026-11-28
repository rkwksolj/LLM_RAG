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

****Note: PDF parsing may lose layout and structural information. Always verify the extracted text manually.****  

**Approach 1: LangChain Document Loaders (Open Source)**  
LangChain provides Document Loaders for parsing documents in various formats.  

- PyPDFLoader: Fast and suitable for simple text-based PDFs.
- PDFPlumber: Better for PDFs with tables and complex layouts.
- UnstructuredLoader: Designed for documents containing mixed content such as text, images, and tables.  

**Approach 2: Amazon Textract (Managed AWS Service)**  
Extract not only text but also document structures such as tables and forms, making it useful for complex and scanned PDFs.  
| Feature | LangChain (PyPDF) | Amazon Textract |
|---------|-------------------|-----------------|
| Text Extraction | O | O |
| Table Structure Recognition | Limited | O (Row/Column Level) |
| Scanned PDF (OCR) | X | O |
| Form (Key-Value) Extraction | X | O |
| Cost | Free (Open Source) | Pay Per Page |
| Setup Complexity | Low | Requires AWS Credentials |  

LangChain and Amazon Textract are complementary tools, and the **choice depends on document characteristics**. First, check whether the *PDF contains selectable text*. If not, *OCR* is required. If text is selectable, evaluate whether *the document contains tables, forms, complex layouts, or mixed content*. For simple text-based PDFs, PyPDFLoader is usually the best starting point.  
<img width="1200" height="800" alt="image" src="https://github.com/user-attachments/assets/ebf1bf71-8be9-49f7-927e-52ff6a6170a2" />
