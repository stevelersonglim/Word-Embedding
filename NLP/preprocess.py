from .vocabularies import Vocabularies

STOPWORDS = {
    "a",
    "about",
    "above",
    "after",
    "again",
    "against",
    "ain",
    "all",
    "also",
    "am",
    "an",
    "and",
    "any",
    "are",
    "aren",
    "aren't",
    "as",
    "at",
    "be",
    "because",
    "been",
    "before",
    "being",
    "below",
    "between",
    "both",
    "but",
    "by",
    "can",
    "couldn",
    "couldn't",
    "d",
    "did",
    "didn",
    "didn't",
    "do",
    "does",
    "doesn",
    "doesn't",
    "doing",
    "don",
    "don't",
    "down",
    "during",
    "each",
    "few",
    "for",
    "from",
    "further",
    "had",
    "hadn",
    "hadn't",
    "has",
    "hasn",
    "hasn't",
    "have",
    "haven",
    "haven't",
    "having",
    "he",
    "her",
    "here",
    "hers",
    "herself",
    "him",
    "himself",
    "his",
    "how",
    "i",
    "if",
    "in",
    "into",
    "is",
    "isbn",
    "isn",
    "isn't",
    "it",
    "it's",
    "its",
    "itself",
    "just",
    "ll",
    "m",
    "ma",
    "me",
    "mightn",
    "mightn't",
    "more",
    "most",
    "mustn",
    "mustn't",
    "my",
    "myself",
    "needn",
    "needn't",
    "no",
    "nor",
    "not",
    "now",
    "o",
    "of",
    "off",
    "on",
    "once",
    "only",
    "or",
    "other",
    "our",
    "ours",
    "ourselves",
    "out",
    "over",
    "own",
    "re",
    "s",
    "same",
    "shan",
    "shan't",
    "she",
    "she's",
    "should",
    "should've",
    "shouldn",
    "shouldn't",
    "so",
    "some",
    "such",
    "t",
    "than",
    "that",
    "that'll",
    "the",
    "their",
    "theirs",
    "them",
    "themselves",
    "then",
    "there",
    "these",
    "they",
    "this",
    "those",
    "through",
    "to",
    "too",
    "under",
    "until",
    "up",
    "ve",
    "very",
    "was",
    "wasn",
    "wasn't",
    "we",
    "were",
    "weren",
    "weren't",
    "what",
    "when",
    "where",
    "which",
    "while",
    "who",
    "whom",
    "why",
    "will",
    "with",
    "won",
    "won't",
    "wouldn",
    "wouldn't",
    "y",
    "you",
    "you'd",
    "you'll",
    "you're",
    "you've",
    "your",
    "yours",
    "yourself",
    "yourselves",
}

def to_sentences(article):
    return article.split(". ")

def remove_commas(sentences):
    return [sentence.replace(',', '') for sentence in sentences]

def remove_punctuations(sentences):
    new_sentences = []
    for sentence in sentences:
        words = sentence.split()
        words = [word for word in words if word != "." and word != ","]
        new_sentences.append(" ".join(words))
    return new_sentences

def remove_rare_characters_by_word_count(article, word_count):
    vocabs = Vocabularies(article)
    list_vocabs = vocabs.list_by_count(ascending=True)
    vocabs_to_be_removed = set()
    for v, c in list_vocabs:
        if c > word_count:
            break
        else:
            vocabs_to_be_removed.add(v)
    new_article = []
    for word in article.split():
        lower_word = word.lower()
        if lower_word not in vocabs_to_be_removed:
            new_article.append(word)

    return " ".join(new_article)


def keep_top_n_vocabularies(article, n):
    vocabs = Vocabularies(article)
    list_vocabs = vocabs.list_by_count()
    vocabs_to_be_added, _ = zip(*list_vocabs[:n])
    vocabs_to_be_added = set(vocabs_to_be_added)

    new_article = []
    for word in article.split():
        lower_word = word.lower()
        if lower_word in vocabs_to_be_added:
            new_article.append(word)

    return " ".join(new_article)


def remove_rare_characters_by_count(article, count):
    vocabs = Vocabularies(article)
    list_vocabs = vocabs.list_by_count(ascending=True)
    vocabs_to_be_removed = set()
    counter = 0
    for v, c in list_vocabs:
        if counter >= count:
            break
        else:
            vocabs_to_be_removed.add(v)
            counter += 1
    new_article = []
    for word in article.split():
        lower_word = word.lower()
        if lower_word not in vocabs_to_be_removed:
            new_article.append(word)

    return " ".join(new_article)


def remove_stop_words(article):
    new_article = []
    for word in article.split():
        lower_word = word.lower()
        if lower_word not in set(STOPWORDS):
            new_article.append(word)
    return " ".join(new_article)