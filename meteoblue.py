import requests
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import requests


load_dotenv()
api_key=str(os.getenv("API_METEOBLUE"))
lat=float(os.getenv("LATITUDE"))
lon=float(os.getenv("LONGITUDE"))

url = (
    f"https://my.meteoblue.com/packages/clouds-1h_seeing-1h"
    f"?lat={lat}&lon={lon}"
    f"&apikey={api_key}"
    f"&format=json"
    f"&tz=Europe/Madrid"
) #https://my.meteoblue.com/packages/redoc#tag/Overview-Structure/paths/~1packages~1%7Bpackages%7D/get

response = requests.get(url)
data=response.json()
print(data)