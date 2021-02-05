import pandas as pd
from io import BytesIO

r = requests.get("https://databank.worldbank.org/data/download/BBSC_CSV.zip", stream=True)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

df = pd.read_csv("BBSCData.csv")
df.head()
