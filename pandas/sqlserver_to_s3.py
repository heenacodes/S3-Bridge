import pandas as pd
from sqlalchemy import create_engine

#source
MYSQL_HOST = "104.237.2.219"
MYSQL_USER = "mysqluser"
MYSQL_PASSWORD = "*7E567C9DC06217268D72D52BABCA14EAB8993ACF"
MYSQL_PORT = 5340
MYSQL_DATABASE_NAME = "demo"

#target
S3_bucket = "s3-heena-demo-session3 "

connection_string = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE_NAME}"
engine = create_engine(connection_string)

df = pd.read_sql("Select * from customers", engine)
print(df.head())
print(df.info())

#transformation



#write to datalake - s3 bucket
df.to_csv("s3://s3-heena-demo-session3/sqlserver_to_s3/customers.json", index=False);

