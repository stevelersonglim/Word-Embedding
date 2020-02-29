from NLP.vocabularies import Vocabularies
from collections import defaultdict
import pandas as pd

class TestVocabularies:
    def test_from_article(self, simple_article):
        vocabs = Vocabularies()
        vocabs.from_article(simple_article)
        df = vocabs._data
        assert len(df.index) == vocabs.total_count
        assert df["index"].nunique() == vocabs.total_count
        assert vocabs._vocabs_with_count == {
            "this": 2,
            "is": 2,
            "a": 2,
            "simple": 2,
            "article": 2,
            "written": 1,
            "by": 1,
            "person": 1,
            "used": 1,
            "to": 1,
            "validate": 1,
            "the": 1,
            "test": 1,
        }

    def test_data(self, simple_string):
        expected = {
            "vocabulary": ["this", "is", "cool"],
            "index": [0, 1, 2],
            "count": [3, 1, 2],
        }
        vocabs = Vocabularies(simple_string)
        test_output = defaultdict(list)
        for _, row in vocabs.to_pandas().iterrows():
            test_output["vocabulary"].append(row["vocabulary"])
            test_output["index"].append(row["index"])
            test_output["count"].append(row["count"])
        assert test_output == expected

    def test_len(self, simple_string):
        vocabs = Vocabularies(simple_string)
        assert len(vocabs) == 3

    def test_list_by_count(self, simple_string):
        vocabs = Vocabularies(simple_string)
        assert vocabs.list_by_count() == [("this", 3), ("cool", 2), ("is", 1)]

    def test_list_by_count_with_n(self, simple_string):
        vocabs = Vocabularies(simple_string)
        assert vocabs.list_by_count(2) == [("this", 3), ("cool", 2)]

    def test_most_common(self, simple_string):
        vocabs = Vocabularies(simple_string)
        assert vocabs.most_common() == "this"

    def test_most_common_with_n(self, simple_string):
        vocabs = Vocabularies(simple_string)
        assert vocabs.most_common(2) == ["this", "cool"]

    def test_get_most_similar_words(self):
        vocabs = Vocabularies("happiness success family hell")
        df = vocabs._data
        df.at[df.index[df["vocabulary"] == "happiness"][0], "vector"] = [1, 1]
        df.at[df.index[df["vocabulary"] == "success"][0], "vector"] = [1, 0.8]
        df.at[df.index[df["vocabulary"] == "family"][0], "vector"] = [1.1, 0.9]
        df.at[df.index[df["vocabulary"] == "hell"][0], "vector"] = [-1, 0]

        assert set(vocabs.get_most_similar_words("happiness", 2)) == {
            "success",
            "family",
        }

    def test_to_pandas(self):
        vocabs = Vocabularies("happiness success family hell")
        df = vocabs.to_pandas()
        df.at[df.index[df["vocabulary"] == "happiness"][0], "index"] = 5
        assert isinstance(df, pd.DataFrame)
        assert vocabs._data.at[vocabs._data.index[vocabs._data["vocabulary"] == "happiness"][0], "index"] == 0

    def test_iter(self, simple_string):
        vocabs = Vocabularies(simple_string)
        expected = ["this", "is", "cool"]
        test_output = [vocab for vocab in vocabs]

        assert expected == test_output

    def test_get_index(self, simple_string):
        vocabs = Vocabularies(simple_string)
        assert vocabs.get_index("this") == 0
        assert vocabs.get_index("is") == 1
        assert vocabs.get_index("cool") == 2

    def test_get_vector(self, simple_string):
        vocabs = Vocabularies(simple_string)
        df = vocabs._data
        df.at[df.index[df["vocabulary"] == "this"][0], "vector"] = [1, 1]
        assert vocabs.get_vector("this") == [1, 1]
        assert vocabs.get_vector("is") is None
