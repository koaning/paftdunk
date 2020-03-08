from paftdunk.datasets import make_blobset
from paftdunk.recommender import Recommender

df = make_blobset()
mod = Recommender().fit(df)
print(mod.itemitem_.head())
print(mod.rec_item_item(item=28))

mod.to_disk("trained-model")
loaded = Recommender.from_disk("trained-model")
print(loaded.itemitem_.head())
print(loaded.rec_item_item(item=28))
