from paftdunk.etl import (
    remove_outliers,
    calc_user_activity,
    calc_item_activity,
    calc_itemitem,
    add_rating,
)
import pathlib
import pandas as pd


class Recommender:
    def __init__(self, k=10):
        self.k = k

    def fit(self, X, y=None):
        self.n_user_ = X.user_id.nunique()
        self.n_item_ = X.item_id.nunique()
        clean_df = remove_outliers(X)
        self.user_popularity_ = calc_user_activity(clean_df)
        self.item_popularity_ = calc_item_activity(clean_df)
        self.itemitem_ = clean_df.pipe(
            calc_itemitem, item_popularity=self.item_popularity_, n_user=self.n_user_
        ).pipe(add_rating)
        return self

    def rec_item_item(self, item, n=None):
        n = self.k if not n else n
        return (
            self.itemitem_.loc[lambda d: d["item_from"] == item]
            .sort_values("rating", ascending=False)
            .head(n)
        )

    def to_disk(self, name):
        base_path = pathlib.Path(name)
        if not base_path.exists():
            base_path.mkdir()
        self.user_popularity_.to_csv(base_path / "user_popularity.csv", index=False)
        self.item_popularity_.to_csv(base_path / "item_popularity.csv", index=False)
        self.itemitem_.to_csv(base_path / "itemitem.csv", index=False)

    @classmethod
    def from_disk(cls, name):
        base_path = pathlib.Path(name)
        rec = Recommender()
        rec.itemitem_ = pd.read_csv(base_path / "itemitem.csv")
        return rec
