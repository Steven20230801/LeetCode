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


# 計算連續>100 3天以上的次數
stadium["over_100"] = stadium["people"] > 100  # 產生一個boolean的column
# 上一天是否一樣大於100
stadium["over_100_yesterday"] = stadium["over_100"].shift(
    1, fill_value=False
)  # 產生一個column，內容是前一天的over_100
stadium["eq"] = (
    stadium["over_100"] == stadium["over_100_yesterday"]
)  # 產生一個column，內容是over_100和over_100_yesterday是否一樣
stadium["group"] = (~stadium["eq"]).cumsum()  # 產生一個group的column
stadium["count"] = stadium.groupby("group")["over_100"].transform(
    "size"
)  # 產生一個count的column
print(stadium)
stadium[stadium["count"] >= 3][["id", "visit_date", "people"]]
