import pandas as pd
import io
import zipfile
from io import BytesIO
import requests

r = requests.get("https://databank.worldbank.org/data/download/BBSC_CSV.zip", stream=True)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

df = pd.read_csv("BBSCData.csv")
print(df.head())
