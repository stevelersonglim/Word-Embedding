import altair as alt
import matplotlib.pyplot as plt
import pandas as pd


class Vocabulary:
    def __init__(self, word, index=None):
        self.name = word
        self._count = 1
        self.vector = None
        self._index = index

    def __repr__(self):
        return "name={name}, count={count} vector={vector}".format(
            name=self.name, count=self._count, vector=self.vector
        )

    @property
    def count(self):
        return self._count

    @property
    def index(self):
        return self._index

    def increment(self):
        self._count += 1


class Vocabularies:
    def __init__(self, articles):
        self._start = -1
        self._vocabs = []
        self.from_article(articles)
        self.get_num = self.__len__()

    def __iter__(self):
        return self

    def __next__(self):
        self._start += 1
        if self._start < self.get_num:
            return getattr(self, self._vocabs[self._start])
        self._start = -1
        raise StopIteration

    def __repr__(self):
        return str(self._vocabs)

    def __len__(self):
        return len(self._vocabs)

    def __getitem__(self, vocab):
        return getattr(self, vocab)

    def from_article(self, article):
        index = 0
        for word in article.split():
            word = word.lower()
            if hasattr(self, word):
                attr = getattr(self, word)
                attr.increment()
            else:
                setattr(self, word, Vocabulary(word, index))
                index += 1
                self._vocabs.append(word)

    def list_vocabs_by_count(self, ascending=False):
        vocabulary_to_count = {vocab: self[vocab].count for vocab in self._vocabs}

        return [
            (k, v)
            for k, v in sorted(
                vocabulary_to_count.items(),
                key=lambda item: item[1],
                reverse=not ascending,
            )
        ]

    def most_common(self):
        return self.list_vocabs_by_count()[0][0]

    def hist(self, n):
        plt.figure()
        F = plt.gcf()
        Size = F.get_size_inches()
        F.set_size_inches(Size[0] * 3, Size[1] * 3, forward=True)
        plt.bar(*zip(*self.list_vocabs_by_count()[:n]))
        plt.ylabel("word count")
        plt.show()

    def to_index(self, word):
        return self[word].index

    def plot(self):
        # this code snippet generates pca diagram
        from collections import defaultdict
        from sklearn.manifold import TSNE
        import pandas as pd

        data = defaultdict(list)
        for vocab in vocabs:
            data["word"].append(vocab.name)
            data["vector"].append(vocab.vector)

        df = pd.DataFrame(data)
        pca_output = TSNE(n_components=2).fit_transform(np.array(list(df["vector"])))
        df["pca1"] = pca_output[:, 0]
        df["pca2"] = pca_output[:, 1]

        alt.renderers.enable("notebook")
        line = (
            alt.Chart(df, title="PCA Embedding Space", height=1000, width=800,)
            .mark_point()
            .encode(x="pca1", y="pca2")
        )

        text = line.mark_text(align="left", baseline="middle", dx=7).encode(text="word")

        return line + text
