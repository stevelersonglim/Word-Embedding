import numpy as np


def compute_X(self, training_data):
    X = np.zeros((len(self), len(self)))
    for data in training_data:
        X[self.get_index(data[0]), self.get_index(data[2])] += 1
    return X


def f(self, x, alpha=3 / 4, x_max=100):
    return (x / x_max) ** alpha if x < x_max else 1

