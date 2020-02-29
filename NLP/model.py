from tensorflow.keras.layers import Embedding, Dense, Flatten
from tensorflow.keras import Sequential


def word2vec(embedding_dim, num_vocabs, batch_size):
    embedding_dim = embedding_dim,
    batch_size = batch_size
    model = Sequential()
    model.add(Embedding(input_dim=num_vocabs, output_dim=embedding_dim, input_length=1))
    model.add(Dense(num_vocabs, activation='softmax', input_shape=(batch_size, embedding_dim)))

    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["sparse_categorical_accuracy"])
    return model

