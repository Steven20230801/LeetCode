import pandas as pd

data = [
    [1, "2017-01-01", 10],
    [2, "2017-01-02", 109],
    [3, "2017-01-03", 150],
    [4, "2017-01-04", 99],
    [5, "2017-01-05", 145],
    [6, "2017-01-06", 1455],
    [7, "2017-01-07", 199],
    [8, "2017-01-09", 188],
]
stadium = pd.DataFrame(data, columns=["id", "visit_date", "people"]).astype(
    {"id": "Int64", "visit_date": "datetime64[ns]", "people": "Int64"}
)


print(stadium)
# >= 100
stadium[">100"] = stadium.people.ge(100)
stadium["shift"] = stadium[">100"].shift(1)
stadium["eq"] = stadium[">100"].eq(stadium["shift"], fill_value=True)
stadium["count"] = stadium.groupby(["eq"])[">100"].cumsum()
stadium
