import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

# get html text from url
response = requests.get(url)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

titles = []
links = []

# store the article headlines and links in lists
for titleline in soup.find_all(name="span", class_="titleline"):
    if titleline.a:
        titles.append(titleline.a.getText())
        links.append(titleline.a.get("href"))

# get the total points/upvotes from each article
scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# scores and headlines are not in the same selector, find the index of the article with the highest score
max_score = max(scores)
max_index = scores.index(max_score)

print(f"Title: {titles[max_index]}")
print(f"Link: {links[max_index]}")
print(f"Score: {max_score}")