import matplotlib.pyplot as plt
import altair as alt
from collections import defaultdict
from sklearn.manifold import TSNE
import pandas as pd
import numpy as np
from .prepare import build_training_data_for_word_embedding, training_data_from_sentences
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
import math

class Vocabulary:

    def __init__(self, name, vector1, vector2, origin):
        self.name = name
        self.vector1 = vector1
        self.vector2 = vector2
        self.origin = origin

    def __repr__(self):
        return self.name

    def __add__(self, other):
        return self.origin.find_closest(np.array(self.vector1) + np.array(other.vector1), [self.name, other.name])

    def __sub__(self, other):
        return self.origin.find_closest(np.array(self.vector1) - np.array(other.vector1), [self.name, other.name])


class Vocabularies:
    def __init__(self, training_data=None):
        self._vocabs_with_count = dict()
        self._data = None
        self._data_cache = None
        self.total_count = None
        if training_data:
            self.from_training_data(training_data)

    def __getitem__(self, word):
        return Vocabulary(word, self.get_vector1(word), self.get_vector2(word), self)

    def __iter__(self):
        return iter(list(self._data["vocabulary"]))

    def __repr__(self):  # pragma: no cover
        return self._data.__repr__()

    def __len__(self):
        return self.total_count

    def from_training_data(self, training_data):
        index = 0
        data = defaultdict(list)

        for word, _ in training_data:
            word = word.lower()
            if word in self._vocabs_with_count:
                self._vocabs_with_count[word] += 1
            else:
                data["vocabulary"].append(word)
                self._vocabs_with_count[word] = 1
                data["index"].append(index)
                index += 1

        for word in data["vocabulary"]:
            data["count"].append(self._vocabs_with_count[word])
        df = pd.DataFrame(data)
        df["vector1"] = None
        df["vector2"] = None
        self._data = df
        self.total_count = len(self._vocabs_with_count)

    def from_sentences(self, sentences):
        index = 0
        data = defaultdict(list)
        for sentence in sentences:
            for word in sentence.split():
                word = word.lower()
                if word in self._vocabs_with_count:
                    self._vocabs_with_count[word] += 1
                else:
                    data["vocabulary"].append(word)
                    self._vocabs_with_count[word] = 1
                    data["index"].append(index)
                    index += 1

        for word in data["vocabulary"]:
            data["count"].append(self._vocabs_with_count[word])
        df = pd.DataFrame(data)
        df["vector"] = None
        self._data = df
        self.total_count = len(self._vocabs_with_count)

    def list_all(self):
        return set(self._vocabs_with_count.keys())

    def from_article(self, article):
        index = 0
        data = defaultdict(list)
        for word in article.split():
            word = word.lower()
            if word in self._vocabs_with_count:
                self._vocabs_with_count[word] += 1
            else:
                data["vocabulary"].append(word)
                self._vocabs_with_count[word] = 1
                data["index"].append(index)
                index += 1

        for word in data["vocabulary"]:
            data["count"].append(self._vocabs_with_count[word])
        df = pd.DataFrame(data)
        df["vector"] = None
        self._data = df
        self.total_count = len(self._vocabs_with_count)

    def list_by_count(self, n=None, ascending=False):
        return self._data.sort_values(by=["count"], ascending=ascending)[["vocabulary", "count"]].head(n)

    def most_common(self, n=1):
        if n == 1:
            return self.list_by_count()[0][0]
        return [item[0] for item in self.list_by_count()[:n]]

    def find_closest(self, vector, tabu_words):
        minimum_error = math.inf
        desired_vector1 = None
        desired_vector2 = None
        desired_vocab =None
        for vocab in self._data["vocabulary"]:
            if vocab in tabu_words:
                continue
            vector1 = self._data[self._data["vocabulary"] == vocab]["vector1"].values[0]
            vector2 = self._data[self._data["vocabulary"] == vocab]["vector2"].values[0]
            error = np.linalg.norm(vector - np.array(vector1))

            if error < minimum_error:
                desired_vector1 = vector1
                desired_vector2 = vector2
                desired_vocab = vocab
                minimum_error = error

        return Vocabulary(desired_vocab, desired_vector1, desired_vector2, self)

    def get_most_similar_words(self, word, n):
        # this code snippet pick top 10 words

        word_vector = self._data[self._data["vocabulary"] == word]["vector1"].values[0]
        cosine_vocab = []

        for vocab in self.list_all():
            if vocab == word:
                continue
            vector = self._data[self._data["vocabulary"] == vocab]["vector1"].values[0]
            cosine_value = np.dot(vector, word_vector) / (
                np.linalg.norm(word_vector) * np.linalg.norm(vector)
            )
            cosine_vocab.append((cosine_value, vocab))

        cosine_vocab = sorted(cosine_vocab, key=lambda x: x[0], reverse=True)

        return [v for _, v in cosine_vocab[:n]]
    
    def output_words(self, word, n):
        # this code snippet pick top 10 words

        word_vector = self._data[self._data["vocabulary"] == word]["vector1"].values[0]
        dot_vocab = []

        for vocab in self.list_all():
            if vocab == word:
                continue
            vector = self._data[self._data["vocabulary"] == vocab]["vector2"].values[0]
            dot_value = np.dot(vector, word_vector) 
            dot_vocab.append((dot_value, vocab))

        dot_vocab = sorted(dot_vocab, key=lambda x: x[0], reverse=True)

        return [v for _, v in dot_vocab[:n]]

    def hist(self, n):  # pragma: no cover
        plt.figure()
        F = plt.gcf()
        Size = F.get_size_inches()
        F.set_size_inches(Size[0] * 3, Size[1] * 3, forward=True)
        plt.bar(*zip(*self.list_by_count()[:n]))
        plt.ylabel("word count")
        plt.show()

    def to_pandas(self):
        return self._data.copy()

    def get_index(self, word):
        df = self._data
        return df[df["vocabulary"] == word]["index"].values[0]

    def get_vector1(self, word):
        df = self._data
        return df[df["vocabulary"] == word]["vector1"].values[0]

    def get_vector2(self, word):
        df = self._data
        return df[df["vocabulary"] == word]["vector2"].values[0]

    def perform_tsne(self):  # pragma: no cover
        df = self._data
        tsne_output = TSNE(n_components=2).fit_transform(np.array(list(df["vector1"])))
        df["tsne1"] = tsne_output[:, 0]
        df["tsne2"] = tsne_output[:, 1]
        return [tuple(item) for item in df[["vocabulary", "tsne1", "tsne2"]].to_numpy()]

    def plot2d(self, n):  # pragma: no cover
        self.perform_tsne()
        df = self._data.sort_values(by='count', ascending=False)[:n]
        alt.renderers.enable("notebook")
        point = (
            alt.Chart(
                df, title="tsne Embedding Space", height=1000, width=800,
            )
            .mark_point()
            .encode(x="tsne1:Q", y="tsne2:Q")
        )

        text = point.mark_text(align="left", baseline="middle", dx=7).encode(
            text="vocabulary:O"
        )

        return point + text

    def keep_top_vocabularies(self, n):
        df = self._data
        df.sort_values(by=["count"], ascending=False)
        self._data_cache = self._data
        self._data = df.head(n)

    def reset(self):
        if self._data_cache is not None:
            self._data = self._data_cache
            self._data_cache = None

    def word_analogy(self, query, analogy):
        word1, word2 = analogy
        output = self.get_vector1(query) - (self.get_vector1(word1) - self.get_vector1(word2))
        tabu_words = [word1, word2, query]
        return self.find_closest(output, tabu_words)
