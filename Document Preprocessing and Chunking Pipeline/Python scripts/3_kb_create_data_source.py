bedrock_agent = boto3.client("bedrock-agent", region_name="us-east-1")

# Add an S3 data source to the Knowledge Base
response = bedrock_agent.create_data_source(
    knowledgeBaseId="YOUR_KB_ID",  # Existing Knowledge Base ID
    name="hr-documents",
    description="HR department document data source",
    dataSourceConfiguration={
        "type": "S3",
        "s3Configuration": {
            "bucketArn": f"arn:aws:s3:::{bucket_name}",
            "inclusionPrefixes": ["hr/"]  # Include only the hr/ folder
        }
    },
    vectorIngestionConfiguration={
        "chunkingConfiguration": {
            "chunkingStrategy": "FIXED_SIZE",
            "fixedSizeChunkingConfiguration": {
                "maxTokens": 512,        # Maximum 512 tokens per chunk
                "overlapPercentage": 20   # 20% overlap
            }
        }
    }
)

data_source_id = response["dataSource"]["dataSourceId"]
print(f"Data source created: {data_source_id}")
