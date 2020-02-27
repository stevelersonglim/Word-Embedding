import matplotlib.pyplot as plt


class Vocabulary:
    def __init__(self, word):
        self.name = word
        self._count = 1
        self._vector_repr = None

    def __repr__(self):
        return "name={name}, count={count}".format(name=self.name, count=self._count)

    @property
    def count(self):
        return self._count

    def increment(self):
        self._count += 1

    @property
    def vector_repr(self):
        return self._vector_repr


class Vocabularies:
    def __init__(self, sentences):
        self.get_vocabs(sentences)

    def __repr__(self):
        return str(self.list_vocabs())

    def __len__(self):
        return len(self.list_vocabs())

    def __getitem__(self, vocab):
        return getattr(self, vocab)

    def get_vocabs(self, article):
        for word in article.split():
            word = word.lower()
            if hasattr(self, word):
                attr = getattr(self, word)
                attr.increment()
            else:
                setattr(self, word, Vocabulary(word))

    def list_vocabs(self):
        return [vocab for vocab in dir(self) if not vocab.startswith("__") and not callable(getattr(self, vocab))]

    def list_vocabs_by_count(self, ascending=False):

        vocabulary_to_count = {
            vocab: getattr(self, vocab).count
            for vocab in dir(self)
            if not vocab.startswith("__") and not callable(getattr(self, vocab))
        }

        return [
            (k, v)
            for k, v in sorted(vocabulary_to_count.items(), key=lambda item: item[1], reverse=not ascending)
        ]

    def most_common(self):
        return self.list_vocabs_by_count()[0][0]

    def hist(self, n):
        plt.figure()
        F = plt.gcf()
        Size = F.get_size_inches()
        F.set_size_inches(Size[0] * 3, Size[1] * 3, forward=True)
        plt.bar(*zip(*self.list_vocabs_by_count()[:n]))
        plt.ylabel('word count')
        plt.show()
