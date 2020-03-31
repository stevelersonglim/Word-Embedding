import tensorflow as tf
import numpy as np


class SkipGram:
    def __init__(self, embedding_size, vocab):
        tf.compat.v1.disable_v2_behavior()
        self.vocab = vocab
        self.vocab_size = len(vocab)
        self.embedding_size = embedding_size
        self.vectors = []

        self.X = None
        self.F = None

    def _build_graph(self):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Embedding(input_dim=self.vocab_size, output_dim=self.embedding_size, input_length=1))
        model.add(tf.keras.layers.Dense(self.vocab_size, activation='softmax', input_dim=self.embedding_size))

        model.compile(optimizer="adam", loss="sparse_categorical_crossentropy",
                      metrics=["sparse_categorical_accuracy"])
        return model

    def fit_vector(self, training_data, epochs=500):

        training_input, training_output = zip(*[(self.get_index(context), self.get_index(target)) for context, target in training_data])

        training_input = tf.reshape(tf.convert_to_tensor(training_input), [len(training_input), 1])
        training_output = tf.reshape(tf.convert_to_tensor(training_output), [len(training_output), 1])

        model = self._build_graph()

        model.fit(training_input, training_output, epochs=epochs)

        for vocab in self.vocab:
            v = np.copy(model.weights[0][self.get_index(vocab)].numpy())
            df = self._data
            df.at[df.index[df["vocabulary"] == vocab][0], "vector"] = v