class Vocabulary:
    def __init__(self, word):
        self.name = word
        self._count = 1
        self._vector_repr = None

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
        self.get_vocabularies(sentences)

    def __repr__(self):
        return str(self.list_vocab())

    def get_vocabularies(self, sentences):
        for sentence in sentences:
            for word in sentence.split():
                word = word.lower()
                if hasattr(self, word):
                    attr = getattr(self, word)
                    attr.increment()
                else:
                    setattr(self, word, Vocabulary(word))

    def list_vocab(self):
        return [vocab for vocab in dir(self) if not vocab.startswith("__")]

    def list_vocab_by_count(self):

        vocabulary_to_count = {
            vocab: getattr(self, vocab).count
            for vocab in dir(self)
            if not vocab.startswith("__") and not callable(getattr(self, vocab))
        }

        return [
            (k, v)
            for k, v in sorted(vocabulary_to_count.items(), key=lambda item: item[1], reverse=True)
        ]

    def most_common(self):

        return self.list_vocab_by_count()[0][0]
