def build_training_data_for_word_embedding(article, window_size):

    training_data = []
    words = article.split()

    for i in range(len(words)):
        for j in range(i - window_size, i + window_size):
            if j < 0 or j == i or j >= len(words):
                continue
            else:
                training_data.append([words[i].lower(), words[j].lower()])

    return training_data