import pandas as pd
import io
import zipfile
from io import BytesIO
import requests
import boto3
# import boto.s3

# from boto3.s3.key import Key
# from secret.py import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

# Request data from world bank - unzip
r = requests.get("https://databank.worldbank.org/data/download/BBSC_CSV.zip", stream=True)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()


# Load data to pandas df
df = pd.read_csv("BBSCData.csv")
df.columns = df.columns.str.replace(' ', '_')
df = df.rename(columns={'2018':'Y2018'})
df.to_csv('BBSCData-clean.csv', index=False)


s3 = boto3.client('s3')
with open("BBSCData-clean.csv", "rb") as f:
        s3.upload_fileobj(f, "434-etl-target", "BBSCData-clean.csv")
