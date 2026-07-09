import boto3
import pandas as pd


def lambda_handler(event, context):
    print("Script started")
    BUCKET = "s3-heena-demo-session3"

    s3 = boto3.client("s3")
    s3.upload_file(
        Filename="erp_data/sales.csv",
        Bucket=BUCKET,
        Key="erp_data/sales.csv"
    )

    s3.upload_file(
        Filename="erp_data/sales2.csv",
        Bucket=BUCKET,
        Key="erp_data/sales2.csv"
    )

    df = pd.read_csv(f"s3://{BUCKET}/erp_data/sales.csv")

    df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
    df['ShipDate'] = pd.to_datetime(df['ShipDate'], errors='coerce')

    is_valid = (
        df['OrderDate'].notna() &
        df['ShipDate'].notna() &
        (df['ShipDate'] >= df['OrderDate']) &
        df['uuid'].notna() &
        df['Country'].notna() &
        (df['UnitCost'] > 0) &
        (df['UnitPrice'] > 0) &
        (df['TotalCost'] > 0)
    )

    valid_df = df[is_valid]
    invalid_df = df[~is_valid]

    print("Writing file to S3...")
    valid_df.to_csv(f"s3://{BUCKET}/processed/valid.csv", index=False)
    invalid_df.to_csv(f"s3://{BUCKET}/processed/invalid.csv", index=False)
    print("Script finished")

    return {
        "statusCode": 200,
        "message": "Success"
    }

if __name__ == "__main__":
    lambda_handler(None, None)