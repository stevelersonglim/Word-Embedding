from NLP.glove import compute_X
from NLP.prepare import training_data_from_sentences
from NLP.mining import *
from NLP.preprocess import *


def test_compute_X(simple_article):
    url = 'https://en.wikipedia.org/wiki/Malaysia'
    article = extract_article_from_wiki(url)
    article = clean(article)
    sentences = to_sentences(article)
    sentences = remove_commas(sentences)
    print(sentences[int(len(sentences)/4):int(len(sentences)*3/4)])

