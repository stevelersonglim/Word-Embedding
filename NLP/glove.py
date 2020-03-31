import tensorflow as tf
import copy


class Glove(object):
    def __init__(self, embedding_size, vocab):
        tf.compat.v1.disable_v2_behavior()
        self.vocab = vocab
        self.vocab_size = len(vocab)
        self.embedding_size = embedding_size
        self.vectors = []

        self.X = None
        self.F = None

    def _build_graph(self, training_data):
        counter = dict()

        # Initialize counter
        for i in range(self.vocab_size):
            for j in range(self.vocab_size):
                counter[(i, j)] = 1

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
        alpha = 3 / 4
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
        self._optimizer = tf.compat.v1.train.AdagradOptimizer(0.01).minimize(self._total_loss)

    def fit(self, training_data, epochs=500):

        self._build_graph(training_data)

        with tf.compat.v1.Session() as session:
            # Step 7: initialize the necessary variables, in this case, w and b
            tf.compat.v1.global_variables_initializer().run()
            # Step 8: train the model for 100 epochs
            for i in range(epochs):
                _, l = session.run([self._optimizer, self._total_loss])
                # Session execute optimizer and fetch values of loss
                print(i, l / len(training_data))

            vectors1, vectors2 = session.run([self.W, self.W_tilde])

        self.vectors1 = vectors1
        self.vectors2 = vectors2

        for v in self.vocab:
            vector1 = vectors1[self.vocab.get_index(v)]
            vector2 = vectors2[self.vocab.get_index(v)]
            df = self.vocab._data
            df.at[df.index[df["vocabulary"] == v][0], "vector1"] = vector1
            df.at[df.index[df["vocabulary"] == v][0], "vector2"] = vector2

        return copy.deepcopy(self.vocab)
