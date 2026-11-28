pip install langchain langchain-community pypdf boto3
from langchain_community.document_loaders import PyPDFLoader

# Load PDF file
FILE_PATH = "./sample_data/company_manual.pdf"
loader = PyPDFLoader(FILE_PATH)
documents = loader.load()

print(f"Total pages: {len(documents)}")
print(f"\n=== Page 1 Content (First 300 Characters) ===")
print(documents[0].page_content[:300])

print(f"\n=== Metadata ===")
print(documents[0].metadata)

# Example output:
# {'source': './sample_data/company_manual.pdf', 'page': 0}
