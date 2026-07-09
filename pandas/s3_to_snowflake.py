import pandas as pd
from sqlalchemy import create_engine

BUCKET = "s3-heena-demo-session3"


SNOWFLAKE_ACCOUNT = "BADCZAU-BPB69017"
SNOWFLAKE_USER = "velmurugan"
SNOWFLAKE_PASSWORD = "June45454464d4f4424"
SNOWFLAKE_WAREHOUSE = "COMPUTE_WH"
SNOWFLAKE_DATABASE = "DEMO2"
SNOWFLAKE_SCHEMA = "DEMO_SCHEMA"
TABLE_NAME = "customers"

# Read CSV from S3
df = pd.read_csv(f"s3://{BUCKET}/sqlserver_to_s3/customers.csv")
print("=== Read from S3 ===")
print(df)
print(f"\nShape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# --- Transformations ---
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

string_cols = df.select_dtypes(include=["object"]).columns
df[string_cols] = df[string_cols].apply(lambda x: x.str.strip() if x.dtype == "object" else x)

df.drop_duplicates(inplace=True)

#df.fillna("", inplace=True)

print(f"\n=== After Transformation ===")
print(f"Shape: {df.shape}")
print(df.head())

# Write to Snowflake
conn_str = (
    f"snowflake://{SNOWFLAKE_USER}:{SNOWFLAKE_PASSWORD}@{SNOWFLAKE_ACCOUNT}/"
    f"{SNOWFLAKE_DATABASE}/{SNOWFLAKE_SCHEMA}?warehouse={SNOWFLAKE_WAREHOUSE}"
)
engine = create_engine(conn_str)

selected_df = df[[
    "cust_id",
    "name",
    "age",
    "gender",
    "city"
]]

print(selected_df.head())

selected_df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False, method="multi")
print(f"\nWritten to Snowflake: {SNOWFLAKE_DATABASE}.{SNOWFLAKE_SCHEMA}.{TABLE_NAME}")

engine.dispose()
