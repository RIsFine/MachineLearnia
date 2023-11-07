import numpy as np
import matplotlib.pyplot as plt


def f(W: np.ndarray[float]):
    n = len(W)

    def z(X: np.ndarray[float]) -> float:
        if X.shape != (n - 1, 1):
            raise ValueError("X size must match W size.")
        return np.vstack((X, 1)).dot(W)
