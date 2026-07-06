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


s3 = boto3.client("s3")
s3.upload_file(
    Filename = "erp_data/sales.csv",
    Bucket = "s3-heena-demo-session3",
    Key = "erp_data/sales.csv"
)