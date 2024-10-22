from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "lxml")

titles = soup.find_all("span", class_="titleline")

scores = soup.find_all("span", class_="score")

most_points = 0
best_article = None
best_link = None

for i in range(len(titles)):
    title_tag = titles[i].find("a")
    title = title_tag.text
    link = title_tag.get("href")

    if i < len(scores):
        score_tag = scores[i]
        points = int(score_tag.text.split()[0])
    else:
        points = 0

    if points > most_points:
        most_points = points
        best_article = title
        best_link = link

    print(f"Title: {title}")
    print(f"Link: {link}")
    print(f"Points: {points}\n")

print(f"The article with the most points is: {best_article}")
print(f"The link to the best article is: {best_link}")
print(f"The number of point of the best article: {most_points}")

