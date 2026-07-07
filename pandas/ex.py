import pandas as pd
import boto3 



BUCKET = "s3-heena-demo-session3"

#pd.set_option("display.max_columns", None)                         //displays all the columns         
#df = pd.read_csv("s3://s3-heena-demo-session3/sales2.csv") 

#To display only columns on Panda
#print(df.columns)
#print(df.info())

#Print first 5 rows of the dataframe
#print(df.head())

#upload data to S3
s3 = boto3.client("s3")
s3.upload_file(
    Filename = "erp_data/sales.csv",
    Bucket = "s3-heena-demo-session3",
    Key = "erp_data/sales.csv"
)

s3.upload_file(
    Filename = "erp_data/sales2.csv",
    Bucket = BUCKET,
    Key = "erp_data/sales2.csv"
)


# Read data from S3
df = pd.read_csv("s3://s3-heena-demo-session3/erp_data/sales.csv")

# Convert dates
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
df['ShipDate'] = pd.to_datetime(df['ShipDate'], errors='coerce')


# Validation rules
is_valid = (
    # Dates should exist
    df['OrderDate'].notna() &
    df['ShipDate'].notna() &

    # Ship date should be after order date
    (df['ShipDate'] >= df['OrderDate']) &

    # Required fields should not be null
    df['uuid'].notna() &
    df['Country'].notna() &

    # Numeric fields should be positive
    (df['UnitCost'] > 0) &
    (df['UnitPrice'] > 0) &
    (df['TotalCost'] > 0)
)


# Split data
valid_df = df[is_valid]
invalid_df = df[~is_valid]


print("Valid records:")
print(valid_df.head())

print("Invalid records:")
print(invalid_df.head())


# Write back to S3
valid_df.to_csv(
    "s3://s3-heena-demo-session3/processed/valid.csv",
    index=False
)

invalid_df.to_csv(
    "s3://s3-heena-demo-session3/processed/invalid.csv",
    index=False
)