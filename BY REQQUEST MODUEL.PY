import requests 

response = requests.get(("https://quotes.toscrape.com/"))
print(response.status_code)
print(response.text)


import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")

data = []

for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").get_text(strip=True)
    author = quote.find("small", class_="author").get_text(strip=True)

    data.append([text, author])

df = pd.DataFrame(data, columns=["Quote", "Author"])

print(df)



import pandas as pd
import requests 

URL = "http://www.omdbapi.com/?i=tt3896198&apikey=852b794d"
response = requests.get(URL)
data = response.status_code
print(data)