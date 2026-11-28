import json
import boto3
from langchain_experimental.text_splitter import SemanticChunker
from langchain.embeddings.base import Embeddings

# Wrapper class to connect Bedrock embeddings with LangChain
class BedrockTitanEmbeddings(Embeddings):
    def __init__(self, region_name="us-east-1"):
        self.client = boto3.client("bedrock-runtime", region_name=region_name)
        self.model_id = "amazon.titan-embed-text-v2:0"

    def embed_documents(self, texts):
        embeddings = []
        for text in texts:
            response = self.client.invoke_model(
                modelId=self.model_id,
                body=json.dumps({"inputText": text})
            )
            result = json.loads(response["body"].read())
            embeddings.append(result["embedding"])
        return embeddings

    def embed_query(self, text):
        return self.embed_documents([text])[0]

# Configure semantic chunking
bedrock_embeddings = BedrockTitanEmbeddings()
semantic_splitter = SemanticChunker(
    bedrock_embeddings,
    breakpoint_threshold_type="percentile"  # Split at the lowest N% of similarity
)

# Split the text
sample_text = documents[0].page_content
semantic_chunks = semantic_splitter.create_documents([sample_text])
print(f"Semantic chunking result: {len(semantic_chunks)} chunks")

# Compare results with and without overlap
splitter_no_overlap = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap=0
)
splitter_with_overlap = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap=100
)

chunks_no = splitter_no_overlap.split_documents(documents)
chunks_yes = splitter_with_overlap.split_documents(documents)

print(f"No overlap: {len(chunks_no)} chunks")
print(f"100-char overlap: {len(chunks_yes)} chunks")
print(f"Additional chunks: {len(chunks_yes) - len(chunks_no)} (+{(len(chunks_yes)/len(chunks_no)-1)*100:.1f}%)")

# Add custom fields to the existing metadata
for chunk in fixed_chunks:
    chunk.metadata["category"] = "HR Policy"
    chunk.metadata["department"] = "HR Team"
    chunk.metadata["created_date"] = "2025-03-01"

# Check the result
print(fixed_chunks[0].metadata)
# Example output:
# {
#   'source': './sample_data/company_manual.pdf',
#   'page': 0,
#   'category': 'HR Policy',
#   'department': 'HR Team',
#   'created_date': '2025-03-01'
# }
