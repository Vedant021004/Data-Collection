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
data1 = response.json()
data2 = response.json()['Ratings']
print(pd.DataFrame(data2))
print("......")
print(data1)
print(".....")
print(data)

import requests 
import pandas as pd
from bs4 import BeautifulSoup


headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    )
}

response = requests.get("https://www.ambitionbox.com/list-of-companies?page=1", headers = headers)

soup = BeautifulSoup(
    response.text,
    'lxml'
)

print(soup.title.text)
print(soup.find('h1').text)
print(soup.find_all('h1')[0].text)
print(soup.find_all('h2')[0].text)


for names in soup.find_all('h2'):
    print(names.text.strip())

rating = soup.find_all(
    "div",
    class_="rating_text rating_text--md"
)
  

for i in rating:
    print(i.text.strip())

print(pd.DataFrame(response).head(10))
# print(response)
# print(response.text)