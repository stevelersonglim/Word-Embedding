import tensorflow as tf
from collections import Counter
import numpy as np
import copy
import math


class Glove(object):
    def __init__(self, embedding_size, vocab):
        tf.compat.v1.disable_v2_behavior()
        # Initialize the weights to `5.0` and the bias to `0.0`
        # In practice, these should be initialized to random values (for example, with `tf.random.normal`)

        #         self.W = []
        #         self.W_tilde = []
        #         self.b = []
        #         self.b_tilde = []

        #         for index in range(len(vocab)):
        #             self.W.append(tf.Variable(tf.zeros((embedding_dimension))))
        #             self.W_tilde.append(tf.Variable(tf.zeros((embedding_dimension))))
        #             self.b.append(tf.Variable(0.))
        #             self.b_tilde.append(tf.Variable(0.))

        #         self.var_list = self.W + self.W_tilde + self.b + self.b_tilde

        self.vocab = vocab
        self.vocab_size = len(vocab)
        self.embedding_size = embedding_size
        self.vectors = []

        self.X = None
        self.F = None

    def _compute_X(self, training_data):
        counter = Counter()

        for word1, word2 in training_data:
            counter[(self.vocab.get_index(word1.lower()), self.vocab.get_index(word2.lower()))] += 1

        X = np.zeros((len(self.vocab), len(self.vocab)))

        for key, value in counter.items():
            X[key[0], key[1]] = value

        self.X = X

    def _compute_f(self, alpha=3 / 4, x_max=100):
        x_max = tf.constant([x_max])
        return tf.minimum(
            1.0,
            tf.pow(
                tf.math.divide(self.X, x_max),
                alpha))


    def loss(self):
        losses = []
        for i in range(len(self.vocab)):
            for j in range(len(self.vocab)):
                if i == j:
                    continue
                else:
                    dummy = tf.tensordot(self.W[i], self.W_tilde[j], 1) + self.b[i] + self.b_tilde[j]
                    dummy = dummy - np.log(self.X[i, j])
                    dummy = tf.math.square(dummy)
                    losses.append(tf.math.scalar_mul(self.F[i, j], dummy))

        return tf.math.add_n(losses)

    def _build_graph(self, training_data):
        counter = Counter()

        for word1, word2 in training_data:
            counter[(self.vocab.get_index(word1.lower()), self.vocab.get_index(word2.lower()))] += 1

        word1 = []
        word2 = []
        X = []

        for words, count in counter.items():
            word1.append(words[0])
            word2.append(words[1])
            X.append(count)

        self.W = tf.Variable(tf.compat.v1.random_uniform([self.vocab_size, self.embedding_size], 1.0, -1.0))
        self.W_tilde = tf.Variable(tf.compat.v1.random_uniform([self.vocab_size, self.embedding_size], 1.0, -1.0))
        b = tf.Variable(tf.compat.v1.random_uniform([self.vocab_size], 1.0, -1.0))
        b_tilde = tf.Variable(tf.compat.v1.random_uniform([self.vocab_size], 1.0, -1.0))

        X = tf.constant(X, dtype=tf.float32)
        alpha = 3/4
        x_max = 100

        f = tf.minimum(
            1.0,
            tf.math.pow(
                tf.math.divide(X, x_max),
                alpha))

        W_embedding = tf.nn.embedding_lookup([self.W], word1)
        W_tilde_embedding = tf.nn.embedding_lookup([self.W_tilde], word2)
        b_embedding = tf.nn.embedding_lookup([b], word1)
        b_tilde_embedding = tf.nn.embedding_lookup([b_tilde], word2)

        embedding_product = tf.math.reduce_sum(tf.math.multiply(W_embedding, W_tilde_embedding), 1)

        log_cooccurrences = tf.math.log(X)

        distance = tf.math.square(tf.math.add_n([
            embedding_product,
            b_embedding,
            b_tilde_embedding,
            tf.math.negative(log_cooccurrences)]))

        self._total_loss = tf.math.reduce_sum(tf.math.multiply(f, distance))
        self._optimizer = tf.compat.v1.train.AdagradOptimizer(0.0001).minimize(self._total_loss)


    def _build_graph_2(self):
        self.W = []
        self.W_tilde = []
        self.b = []
        self.b_tilde = []
        self.f = self._compute_f()

        for index in range(self.vocab_size):
            self.W.append(tf.Variable(tf.compat.v1.random_uniform([self.embedding_size], 1.0, -1.0)))
            self.W_tilde.append(tf.Variable(tf.compat.v1.random_uniform([self.embedding_size], 1.0, -1.0)))
            self.b.append(tf.Variable(tf.compat.v1.random_uniform([1], 1.0, -1.0)))
            self.b_tilde.append(tf.Variable(tf.compat.v1.random_uniform([1], 1.0, -1.0)))

        losses = []
        for i in range(self.vocab_size):
            for j in range(self.vocab_size):
                if i == j or self.X[i, j] == 0:
                    continue
                else:
                    dummy = tf.tensordot(self.W[i], self.W_tilde[j], 1) + self.b[i] + self.b_tilde[j]
                    dummy = dummy - np.log(self.X[i, j])
                    dummy = tf.math.square(dummy)
                    losses.append(tf.math.scalar_mul(self.f[i, j], dummy))

        self.__total_loss = tf.math.add_n(losses)

        self.__optimizer = tf.compat.v1.train.AdagradOptimizer(100).minimize(self.__total_loss)

    def _build_graph_3(self, training_data):
        counter = Counter()

        for word1, word2 in training_data:
            counter[(self.vocab.get_index(word1.lower()), self.vocab.get_index(word2.lower()))] += 1

        word1 = []
        word2 = []
        X = []

        for words, count in counter.items():
            word1.append(words[0])
            word2.append(words[1])
            X.append(count)


    def fit(self, training_data, epochs=500):
        self._build_graph(training_data)

        with tf.compat.v1.Session() as session:
            # Step 7: initialize the necessary variables, in this case, w and b
            tf.compat.v1.global_variables_initializer().run()
            print("Initialized")
            # Step 8: train the model for 100 epochs
            for i in range(epochs):
                _, l = session.run([self._optimizer, self._total_loss])
                # Session execute optimizer and fetch values of loss
                print(i, l/len(training_data))

            vectors = session.run([self.W])

        for v in self.vocab:
            vector = vectors[0][self.vocab.get_index(v)]
            df = self.vocab._data
            df.at[df.index[df["vocabulary"] == v][0], "vector"] = vector

        return copy.deepcopy(self.vocab)
