from bs4 import BeautifulSoup

with open("E:\Lucy\web_scraping\index1.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# print(doc.prettify())

tag = doc.title
print(tag)
print(tag.string)

