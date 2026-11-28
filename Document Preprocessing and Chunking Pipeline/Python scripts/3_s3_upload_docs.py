import boto3
import json

s3_client = boto3.client("s3", region_name="us-east-1")
bucket_name = "my-rag-documents"

# 1. Create an S3 bucket
s3_client.create_bucket(Bucket=bucket_name)
print(f"Bucket created: {bucket_name}")

# 2. Upload a PDF document
s3_client.upload_file(
    Filename="./sample_data/company_manual.pdf",
    Bucket=bucket_name,
    Key="hr/company_manual.pdf"
)
print("PDF uploaded successfully")

# 3. Create and upload a metadata file
metadata = {
    "metadataAttributes": {
        "category": "HR Policy",
        "department": "HR",
        "year": 2025
    }
}

s3_client.put_object(
    Bucket=bucket_name,
    Key="hr/company_manual.pdf.metadata.json",
    Body=json.dumps(metadata, ensure_ascii=False),
    ContentType="application/json"
)
print("Metadata uploaded successfully")
