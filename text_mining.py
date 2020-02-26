import requests
from bs4 import BeautifulSoup
#count the number of vocabularies in the article


def clean_sentence(sentence):
    # Remove non-alphanumeric characters
    words = sentence.split()
    words = [word for word in words if word.isalnum()]
    return ' '.join(words)


def extract_sentences_from_wiki(url):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    whitelist = ['p', 'a']
    unclean_output = ''
    for t in text:
        if t.parent.name in whitelist:
            unclean_output += '{} '.format(t)

    unclean_output = unclean_output.split(". ")
    clean_output = []

    for sentence in unclean_output:
        clean_output.append(clean_sentence(sentence))

    return clean_output
