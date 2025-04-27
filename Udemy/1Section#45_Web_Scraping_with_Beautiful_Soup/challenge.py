from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)
article_tag = soup.find(name="span", class_="titleline")
article_text = article_tag.getText()
#article_link = article_text
print(article_text)
