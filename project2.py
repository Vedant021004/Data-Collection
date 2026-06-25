import requests 
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com")
response.encoding = "utf-8"
print(response.status_code)
# print(response.text.strip())

soup = BeautifulSoup(
    response.text,
    'lxml'
)




data = soup.find_all("h3")
for name in data:
    print(name.text)

data2 = soup.find_all(
    "p",
    class_= "price_color"
)
for price in data2:
    print(price.text)


data3 = soup.find_all(
    "p",
    class_ = "instock availability"
)

for stock in data3:
    print(stock.text.strip())

books = []
for name, price, stock in zip(data, data2, data3):
    books.append({
           "Title" : name.text,
           "Rate"  :  price.text.strip(),
           "Availability"  :  stock.text.strip()
    })
df = pd.DataFrame(books)
print(df)