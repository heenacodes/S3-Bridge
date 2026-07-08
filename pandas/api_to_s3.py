import pandas as pd
import requests
import boto3
import json
from io import StringIO
from datetime import datetime

s3_client = boto3.client('s3')
bucket = "s3-heena-demo-session3"

def fetch_weather_data():
    city = "London"
    api_key = "50b2bd8f55249bb2230280600de16d97"
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(api_url)
    return response.json()

def upload_to_s3(data):
    file_name = f"api_data/weather_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    s3_client.put_object(Bucket=bucket, Key=file_name, Body=json.dumps(data))
    return file_name


weather_data=fetch_weather_data()
s3_path=upload_to_s3(weather_data)
print(json.dumps(weather_data, indent=2))
print("uploaded to", s3_path)

