# S3 Bridge

Bridge ERP data files to AWS S3 using Python (boto3 + pandas).

## Data Files

- `erp_data/sales.csv` — Sales data (111 KB)
- `erp_data/sales2.csv` — Additional sales data (2 KB)

## S3 Bucket

Data is uploaded to `s3://s3-heena-demo-session3/`.

## Usage

```bash
# Upload data files to S3
aws s3 cp erp_data/sales.csv s3://s3-heena-demo-session3/
aws s3 cp erp_data/sales2.csv s3://s3-heena-demo-session3/

# List contents of the bucket
aws s3 ls s3://s3-heena-demo-session3/
```

## Setup

```bash
pip install -r requirements.txt
``` 