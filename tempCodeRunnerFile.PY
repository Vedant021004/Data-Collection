import pandas as pd
import requests 

URL = "http://www.omdbapi.com/?i=tt3896198&apikey=852b794d"
response = requests.get(URL)
data = response.status_code
print(data)