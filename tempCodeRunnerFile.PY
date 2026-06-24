
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
    print(names.text)