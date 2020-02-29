import matplotlib.pyplot as plt
import altair as alt
from collections import defaultdict
from sklearn.manifold import TSNE
import pandas as pd
import numpy as np
from .prepare import build_training_data_for_word_embedding
import tensorflow as tf
from .model import word2vec

class Vocabularies:
    def __init__(self, article=None, fit=False):
        self._vocabs_with_count = dict()
        self._data = None
        self.total_count = None
        if article:
            self.from_article(article)
        if fit:
            self.fit_vector(article)

    def __iter__(self):
        return iter(list(self._data["vocabulary"]))

    def __repr__(self):  # pragma: no cover
        return self._data.__repr__()

    def __len__(self):
        return self.total_count

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
        df["tse1"] = None
        df["tse2"] = None
        self._data = df
        self.total_count = len(self._vocabs_with_count)

    def list_by_count(self, n=None, ascending=False):
        sorted_list = [
            (k, v)
            for k, v in sorted(
                self._vocabs_with_count.items(),
                key=lambda item: item[1],
                reverse=not ascending,
            )
        ]
        if n:
            return sorted_list[:n]
        return sorted_list

    def most_common(self, n=1):
        if n == 1:
            return self.list_by_count()[0][0]
        return [item[0] for item in self.list_by_count()[:n]]

    def get_most_similar_words(self, word, n):
        # this code snippet pick top 10 words

        word_vector = self._data[self._data["vocabulary"] == word]["vector"].values[0]
        cosine_vocab = []

        for vocab in self.list_all():
            if vocab == word:
                continue
            vector = self._data[self._data["vocabulary"] == vocab]["vector"].values[0]
            cosine_value = np.dot(vector, word_vector) / (
                np.linalg.norm(word_vector) * np.linalg.norm(vector)
            )
            cosine_vocab.append((cosine_value, vocab))

        cosine_vocab = sorted(cosine_vocab, key=lambda x: x[0], reverse=True)

        return [v for _, v in cosine_vocab[:n]]

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

    def get_vector(self, word):
        df = self._data
        return df[df["vocabulary"] == word]["vector"].values[0]

    def perform_tsne(self):  # pragma: no cover
        df = self._data
        tsne_output = TSNE(n_components=2).fit_transform(np.array(list(df["vector"])))
        df["tse1"] = tsne_output[:, 0]
        df["tse2"] = tsne_output[:, 1]
        return [tuple(item) for item in df[["vocabulary", "tse1", "tse2"]].to_numpy()]

    def plot(self):  # pragma: no cover
        self.perform_tsne()

        alt.renderers.enable("notebook")
        point = (
            alt.Chart(
                self._data, title="PCA Embedding Space", height=1000, width=800,
            )
            .mark_point()
            .encode(x="tse1", y="tse2")
        )

        text = point.mark_text(align="left", baseline="middle", dx=7).encode(
            text="word"
        )

        return point + text

    def fit_vector(self, article, window_size=2, embedding_dim=None, batch_size=None, epoch=1000):
        training_data = build_training_data_for_word_embedding(article, window_size)

        training_input, training_output = zip(*[(self.get_index(context), self.get_index(target)) for context, target in training_data])

        training_input = tf.reshape(tf.convert_to_tensor(training_input), [len(training_input), 1])
        training_output = tf.reshape(tf.convert_to_tensor(training_output), [len(training_output), 1])

        if not embedding_dim:
            embedding_dim = int(0.5 * len(self))
        if not batch_size:
            batch_size = int(0.3 * len(training_data))

        model = word2vec(embedding_dim, len(self), batch_size)
        model.fit(training_input, training_output, epochs=100000, batch_size=batch_size)

        for vocab in self:
            v = np.copy(model.weights[0][self.get_index(vocab)].numpy())
            df = self._data
            df.at[df.index[df["vocabulary"] == vocab][0], "vector"] = v
            vocab.vector = v
