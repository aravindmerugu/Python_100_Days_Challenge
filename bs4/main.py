from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
anchor_tags = soup.findAll(name="a", class_="titlelink")
scores = soup.findAll(name="span",class_="score")
anchor_text = [a.getText() for a in anchor_tags]
anchor_link = [a.get("href") for a in anchor_tags]
scores = [int(score.getText().split()[0]) for score in scores]
#print(anchor_text)
# print(anchor_link)
# print(scores)
max_index = scores.index(max(scores))
print(max(scores),max_index)
print(f"{anchor_text[max_index]}\n{anchor_link[max_index]}\n{scores[max_index]}")
# #import lxml
#
# with open("website.html", encoding='utf-8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags = soup.findAll(name="a")
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     #print(tag.get("href"))
#     pass
#
# print(soup.find(name="h1", id="name"))
# print(soup.find(name="h3", class_="heading"))
# print(soup.select_one("p a").get("href"))
# print(soup.select_one("#name"))