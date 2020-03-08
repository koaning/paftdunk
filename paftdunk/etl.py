from itertools import chain

import pandas as pd

from paftdunk.common import counting_window
from paftdunk.ratings import serendipity


def start_pipeline(dataf, **kwargs):
    return dataf.copy()


def remove_outliers(dataf, min_items_per_user=0, min_users_per_item=0, **kwargs):
    user_df = calc_user_activity(dataf)
    item_df = calc_item_activity(dataf)
    bad_users = user_df.loc[lambda d: d["n_uniq_item"] < min_items_per_user].user_id
    bad_items = item_df.loc[lambda d: d["n_uniq_user"] < min_users_per_item].item_id
    return dataf.loc[lambda d: ~d["user_id"].isin(bad_users)].loc[
        lambda d: ~d["item_id"].isin(bad_items)
    ]


def calc_overlap_df(dataf, **kwargs):
    agg_df = dataf.groupby("user_id").apply(lambda d: list(d["item_id"]))
    chain_of_window = chain(*(list(counting_window(i[1])) for i in agg_df.items()))
    return (
        pd.DataFrame(chain_of_window, columns=["item_from", "item_id"])
        .assign(n=1)
        .groupby(["item_from", "item_id"])
        .agg(n_overlap=("n", "count"))
        .reset_index()
    )


def calc_itemitem(dataf, item_popularity, n_user, min_overlap=5, **kwargs):
    return (
        dataf.pipe(calc_overlap_df)
        .loc[lambda d: d["n_overlap"] >= min_overlap]
        .set_index("item_id")
        .join(item_popularity.set_index("item_id"))
        .reset_index()
        .rename(
            columns={
                "item_id": "item_to",
                "item_from": "item_id",
                "n_uniq_user": "n_uniq_to",
            }
        )
        .set_index("item_id")
        .join(item_popularity.set_index("item_id"))
        .reset_index()
        .rename(columns={"item_id": "item_from", "n_uniq_user": "n_uniq_from"})
        .assign(n_total_user=n_user)
    )


def calc_user_activity(dataf, **kwargs):
    return (
        dataf.groupby("user_id").agg(n_uniq_item=("item_id", "nunique")).reset_index()
    )


def calc_item_activity(dataf, **kwargs):
    return (
        dataf.groupby("item_id").agg(n_uniq_user=("user_id", "nunique")).reset_index()
    )


def add_rating(dataf, setting="serendipity", **kwargs):
    if setting == "serendipity":
        return dataf.assign(rating=serendipity(alpha=1, beta=1))
    raise ValueError(f"Rating setting {setting} is unknown.")
