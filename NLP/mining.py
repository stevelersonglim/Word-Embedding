import requests
from bs4 import BeautifulSoup

from .old_code import Vocabularies


def extract_article_from_wiki(url):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, "html.parser")
    # text = soup.find_all(text=True)
    # whitelist = ["p", "a"]
    # article = ""
    # for t in text:
    #     if t.parent.name in whitelist:
    #         article += "{} ".format(t)
    text = soup.get_text()
    return text


def clean(text):
    text = text[text.find('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')+1:text.find('\n\nSee also')]
    sentences = " ".join(text.split("\n")).split(".")
    new_sentences = []
    for sentence in sentences:
        words = sentence.split()
        words = [word for word in words if not ("[" and "]" in word)]
        new_sentences.append(" ".join(words))
    return ". ".join(new_sentences)


def remove_references(text):
    return text[:text.find('\n\n\nReferences\n\n\n')]


def remove_table_of_content(text):
    text.find('\n\nContents')


