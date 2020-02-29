import requests
from bs4 import BeautifulSoup

from .old_code import Vocabularies


def extract_article_from_wiki(url):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, "html.parser")
    text = soup.find_all(text=True)
    whitelist = ["p", "a"]
    article = ""
    for t in text:
        if t.parent.name in whitelist:
            article += "{} ".format(t)
    return article

