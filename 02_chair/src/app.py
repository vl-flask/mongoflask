import requests
from bs4 import BeautifulSoup

# req = requests.get("https://google.com")

req = requests.get("https://www.johnlewis.com/john-lewis-reid-faux-leather-office-chair/p3176358")
content = req.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price price--large"})
# <p class="price price--large">£179.00</p>
string_price = element.text.strip()
price = float(string_price[1:])
print(string_price)
# print(price)
# print(price < 200)
# print(req.content)
if price < 200:
    print("Buy it")
    print(f"The current price is {price}")
else:
    print("Don't buy it")
