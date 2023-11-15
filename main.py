import csv
import requests
from bs4 import BeautifulSoup

data = requests.get("https://en.wikipedia.org/wiki/Requests_(software)")

soup = BeautifulSoup(data.text, features="html.parser")

text = [["text"]]
div = soup.find_all("div", {"class": "mw-parser-output"})
for d in div:
    p = d.find_all("p")
    for v in p:
        text.append([v.text.strip()])

with open('text.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(text)