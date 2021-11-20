<img src="docs/paftdunk.png" width=175 height=175 align="right" />

# PaftDunk

> Recommendin' all night to get lucky. Smaller, Lighter, Simpler, Calmer. 

The **PaftDunk** library tries to achieve recommendations by ... simply counting. It is meant as a dead simple, minimal (and calm) starting point. It's not meant to be state of the art or anything. But should make help you with some simple benchmarks and analyses. 

## IMPORTANT 

This readme is but an API spec. This is not implemented yet.

## Command Line 

You can use different engines to calculate recommendations. Initially we'd like to support pandas, polars, dask and spark.

```
> paftdunk rec --engine polars --src logs.parquet --out rec_out
```

This will generate files in the `rec_out` folder. 

```
metadata.json
item_to_item.parquet
item_to_user.parquet
user_to_item.parquet
user_to_user.parquet
```

The idea is that these files are pre-calculated recommendations. These can either be moves into a cache like redits or be used to directly serve recommendations.
