import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

titles = []
links = []
scores = []

for titleline in soup.find_all(name="span", class_="titleline"):
    if titleline.a:
        titles.append(titleline.a.getText())
        links.append(titleline.a.get("href"))

for score in soup.find_all(name="span", class_="score"):
    scores.append(int(score.getText().split()[0]))

max_score = max(scores)
max_index = scores.index(max_score)

print(f"Title: {titles[max_index]}")
print(f"Link: {links[max_index]}")
print(f"Score: {max_score}")