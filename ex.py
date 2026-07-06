import pandas as pd

BUCKET = "s3-heena-demo-session3"
df = pd.read_csv("s3://s3-heena-demo-session3/sales2.csv") 

print (df)
