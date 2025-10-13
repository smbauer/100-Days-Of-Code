import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

movies_list = [movie.get_text() for movie in soup.find_all(name="h3", class_="title")]
movies_list.reverse()

with open("top_100_movies/movies.txt", "w", encoding="utf-8") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")