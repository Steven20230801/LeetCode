import pandas as pd
import numpy as np


data = [[1, "Avengers"], [2, "Frozen 2"], [3, "Joker"]]
movies = pd.DataFrame(data, columns=["movie_id", "title"]).astype(
    {"movie_id": "Int64", "title": "object"}
)
data = [[1, "Daniel"], [2, "Monica"], [3, "Maria"], [4, "James"]]
users = pd.DataFrame(data, columns=["user_id", "name"]).astype(
    {"user_id": "Int64", "name": "object"}
)
data = [
    [1, 1, 3, "2020-01-12"],
    [1, 2, 4, "2020-02-11"],
    [1, 3, 2, "2020-02-12"],
    [1, 4, 1, "2020-01-01"],
    [2, 1, 5, "2020-02-17"],
    [2, 2, 2, "2020-02-01"],
    [2, 3, 2, "2020-03-01"],
    [3, 1, 3, "2020-02-22"],
    [3, 2, 4, "2020-02-25"],
]
movie_rating = pd.DataFrame(
    data, columns=["movie_id", "user_id", "rating", "created_at"]
).astype(
    {
        "movie_id": "Int64",
        "user_id": "Int64",
        "rating": "Int64",
        "created_at": "datetime64[ns]",
    }
)


from datetime import date


# 1. group user_id sum count user_id numbers
df = movie_rating.groupby("user_id").size().reset_index(name="size")
df = df[
    (df["size"] == df["size"].max()) & (df["user_id"] == df["user_id"].min())
].merge(users, on="user_id")[["name"]]


# 2.
movie_rating = movie_rating[
    (movie_rating["created_at"].dt.date >= date(2020, 2, 1))
    & (movie_rating["created_at"].dt.date <= date(2020, 2, 29))
]
