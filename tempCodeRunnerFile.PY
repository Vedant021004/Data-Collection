import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd



headers = {
    "User-Agent": "Mozilla/5.0"
}

all_names = []
all_prices = []
all_description = []
all_stars = []
all_reviews = []

for page in range(1, 3):
    url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={page}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    data = soup.find_all("a", class_="title")
    data2 = soup.find_all("h4", class_="price")
    data3 = soup.find_all("p", class_="description")
    rating = soup.find_all("p", attrs={"data-rating": True})
    data4 = soup.find_all("p", class_ = "review-count")

    for item in data:
        all_names.append(item.text.strip())

    for rate in data2:
        all_prices.append(rate.text.strip())

    for description in data3:
        all_description.append(description.text.strip())  

    for stars in rating:
        all_stars.append(stars["data-rating"])

    for feedback in data4:
        all_reviews.append(feedback.text.strip())    


for name, price, description, rating, review in zip(
    all_names,
    all_prices,
    all_description,
    all_stars,
    all_reviews
):
    print(f"""
Name        : {name}
Price       : {price}
Description : {description}
Rating      : {rating}
Reviews     : {review}
{'-'*60}
""")        
