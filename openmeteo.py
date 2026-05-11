import requests
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import requests


load_dotenv()
lat=float(os.getenv("LATITUDE"))
lon=float(os.getenv("LONGITUDE"))

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude":lat,
	"longitude": lon,
	"hourly": ["temperature_2m", "cloud_cover", "cloud_cover_low", "cloud_cover_mid", "cloud_cover_high", "visibility"],
    "models": "ecmwf_ifs",
	"timezone": "auto",
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data["hourly"])
df["time"] = pd.to_datetime(df["time"])
df.set_index("time", inplace=True)
print(df)