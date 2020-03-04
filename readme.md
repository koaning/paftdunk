<a href="/docs/logo.png"><img src="docs/logo.png" width="35%" height="35%" align="right" /></a>

# PaftDunk

> It's recommending all night to get lucky. - Paft Dunk

The **PaftDunk** library tries to achieve recommendations by ... simply counting. It is meant as a dead simple, minimal (and calm) starting point.

## QuickStart 

We assume that you've got a pandas dataframe containing all the interactions between users and items that have occurred. 

```python
import pandas as pd
df = pd.read_csv("<path>/<file>.csv")
df.head(3)
#    user  item
# 0     1     3
# 1     2     4
# 2     3     5
```

This dataframe can be passed to a new `PaftDunk` object. 

```python
from paftdunk import Recommender 

model = Recommender()
model.fit(df)
```

This model can now make all sorts of predictions. 

```python
model.rec_user_user(user=2, n=5)
model.rec_user_item(user=2, n=5)
model.rec_item_user(item=3, n=5)
model.rec_item_item(item=5, n=5)
```

## Settings

You can customise the settings of the recommendation.

```python
model = Recommender(k=5, method="overlap", fallback="popular")
model.fit(X=df, y=df['margin'])
```

By setting `k` and `method` you determine that this recommender is meant
to recommend 5 items in general using the `overlap` method. If it cannot
recommend anything (perhaps due to a cold start) it will fall back to the
`popular` fallback method. During training we also specify a `y` parameter
that will allow us to tell the algorithm to weight certain user/product 
combinations as more or less valueable. For example, the margin of a product
can be passed here. 

## Development 

Install `paftdunk` in the virtual environment via:

```bash
$ pip install --editable .
```
