import pandas as pd


df = pd.read_csv("input.csv")
query_df = pd.read_csv("query.csv")

out = []
for idx, row in query_df.iterrows():
    diffs = (
        df.loc[
            df[row["genre"]]
            & (df["year"] >= row["min_year"])
            & (df["year"] <= row["max_year"]),
            ["x", "y"],
        ]
        - row
    )
    squares = diffs**2
    dists = squares.sum(axis=1) ** 0.5

    closest_idx = dists.sort_values().index[0]
    out.append(df.loc[closest_idx, ["year", "title", "imdb_id"]].to_dics())

pd.DataFrame(out).to_csv("out.csv", index=False)
