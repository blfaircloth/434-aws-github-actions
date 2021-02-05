import pandas as pd
import io
import zipfile
from io import BytesIO
import requests
import boto3

# Request data from world bank - unzip
r = requests.get("https://databank.worldbank.org/data/download/BBSC_CSV.zip", stream=True)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()


# Load data to pandas df
df = pd.read_csv("BBSCData.csv")
print(df.head())


#s3 = boto3.resource('s3')
#bucket = s3.Bucket('434-etl-target')
#s3.object('434-etl-target', 'BBSCdata.csv').put(Body=open('tmp/BBSCData.csv')) 


s3 = boto3.client('s3')
with open("BBSCData.csv", "rb") as f:
        s3.upload_fileobj(f, "434-etl-target", "BBSCData.csv")
