from paftdunk.datasets import make_blobset
from paftdunk.recommender import Recommender

df = make_blobset()
mod = Recommender().fit(df)
print(mod.itemitem_.head())
print(mod.rec_item_item(item=28))
