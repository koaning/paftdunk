import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs


def make_blobset(random_state=42):
    X, y = make_blobs(n_samples=50000, centers=20, random_state=random_state)
    X = np.round(X * 10)
    X += np.abs(np.min(X))
    return pd.DataFrame(X, columns=["user_id", "item_id"]).astype(int)
