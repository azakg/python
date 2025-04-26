from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name = "a")

for tag in all_anchor_tags:
    str1 = str(tag)
    str_mutch = "https://angelabauer.github.io/cv/hobbies.html"
    if str_mutch in str1:
        print(tag.get("href"))

h1_item = soup.find(name = "h1", id = 'name')
print(h1_item)
h1_item1 = soup.find(name = "h1", id = "name1")
print(h1_item1)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)
name1 = soup.select_one(selector="#name1")
print(name1)