import boto3

# Create Textract client
textract_client = boto3.client("textract", region_name="us-east-1")

# Analyze a PDF stored in S3 (asynchronous mode, suitable for multi-page PDFs)
response = textract_client.start_document_analysis(
    DocumentLocation={
        "S3Object": {
            "Bucket": "my-rag-documents",
            "Name": "company_manual.pdf"
        }
    },
    FeatureTypes=["TABLES", "FORMS"]  # Extract tables and forms as well
)

job_id = response["JobId"]
print(f"Started Textract analysis job: {job_id}")

import time

# Wait for analysis to complete
while True:
    result = textract_client.get_document_analysis(JobId=job_id)
    status = result["JobStatus"]

    if status in ["SUCCEEDED", "FAILED"]:
        break

    print(f"Analysis in progress... (Status: {status})")
    time.sleep(5)

if status == "SUCCEEDED":
    # Check extracted text blocks
    blocks = result["Blocks"]
    text_blocks = [b for b in blocks if b["BlockType"] == "LINE"]

    print(f"Number of extracted text lines: {len(text_blocks)}")

    for block in text_blocks[:5]:
        print(block["Text"])
