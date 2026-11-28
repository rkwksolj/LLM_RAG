# Start the data source sync (ingestion)
sync_response = bedrock_agent.start_ingestion_job(
    knowledgeBaseId="YOUR_KB_ID",
    dataSourceId=data_source_id
)

ingestion_job_id = sync_response["ingestionJob"]["ingestionJobId"]
print(f"Sync job started: {ingestion_job_id}")

import time

# Check sync status
while True:
    job = bedrock_agent.get_ingestion_job(
        knowledgeBaseId="YOUR_KB_ID",
        dataSourceId=data_source_id,
        ingestionJobId=ingestion_job_id
    )
    status = job["ingestionJob"]["status"]

    if status in ["COMPLETE", "FAILED"]:
        break

    print(f"Sync in progress... (Status: {status})")
    time.sleep(10)

if status == "COMPLETE":
    stats = job["ingestionJob"]["statistics"]
    print("Sync completed!")
    print(f"  - Documents scanned: {stats.get('numberOfDocumentsScanned', 0)}")
    print(f"  - New documents indexed: {stats.get('numberOfNewDocumentsIndexed', 0)}")
    print(f"  - Modified documents indexed: {stats.get('numberOfModifiedDocumentsIndexed', 0)}")
    print(f"  - Documents deleted: {stats.get('numberOfDocumentsDeleted', 0)}")
else:
    print(f"Sync failed: {job['ingestionJob'].get('failureReasons', 'Unknown')}")
