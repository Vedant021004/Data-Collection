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