import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movies_webpage = response.text
soup = BeautifulSoup(movies_webpage, "html.parser")

titles = soup.findAll(name="h3",class_="title")
title_names = [title.getText() for title in titles]
movies = title_names[::-1]
print(movies)
with open("movies.txt","w") as file:
    for movie in movies:
        file.write(f'{movie}\n')



