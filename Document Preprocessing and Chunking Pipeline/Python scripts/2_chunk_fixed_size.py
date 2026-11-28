from langchain.text_splitter import RecursiveCharacterTextSplitter

# Configure the fixed-size splitter
fixed_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,       # About 500 characters per chunk
    chunk_overlap=50,     # Overlap of about 50 characters
    separators=["\n\n", "\n", " ", ""]  # Split priority
)

# Split the documents
fixed_chunks = fixed_splitter.split_documents(documents)
print(f"Fixed-size chunking result: {len(fixed_chunks)} chunks")

# Check the first chunk
print(f"\n=== Chunk 1 ({len(fixed_chunks[0].page_content)} chars) ===")
print(fixed_chunks[0].page_content[:200])
