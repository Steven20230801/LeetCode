import pandas as pd

data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
logs = pd.DataFrame(data, columns=["id", "num"]).astype({"id": "Int64", "num": "Int64"})


# 标记相同数字
logs["SameAsPrevious"] = logs["num"].eq(logs["num"].shift(1, fill_value=True))

# 使用 cumsum 创建组标识符
logs["Group"] = (~logs["SameAsPrevious"]).cumsum()

# 对每个组内相同数字的出现次数进行计数
logs["Count"] = logs.groupby("Group")["num"].transform("count")

# 筛选出现次数至少为 3 的组
logs[logs["Count"] >= 3][["num"]].drop_duplicates().rename(
    columns={"num": "ConsecutiveNums "}
)


logs

logs["shift eq num"] = logs["num"].eq(logs["num"].shift(1))
logs["count"] = logs.groupby("num")["shift eq num"].cumsum()
logs["not eq"] = ~logs["shift eq num"]
logs["Group"] = (~logs["shift eq num"]).cumsum()
logs["max"] = logs.groupby("num")["count"].max()
logs


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs["shiht1"] = logs["num"].shift(1)
    logs["count"] = logs["num"].ne(logs["shiht1"]).cumsum()
    return logs.groupby("num")["count"].max()


# 計算各個連續出現次數
# logs["count"] = logs.groupby("num").cumcount() + 1
# print(logs)

# group by rolling
logs["count"] = logs.groupby("num")["num"].rolling(3).count().reset_index(0, drop=True)

print(logs)

# 計算num 連續相依出現的次數
logs["shiht1"] = logs["num"].shift(1)
logs["shift eq num"] = logs["num"].ne(logs["shiht1"])
logs["count"] = logs["num"].ne(logs["shiht1"]).cumsum()
logs["max"] = logs.groupby("num")["count"].max()
logs["t_max"] = logs.groupby("num")["count"].transform("max")

# logs["num"].ne(logs["num"].shift(1))
print(logs)


logs.groupby(logs["num"].ne(logs["shiht1"].shift()).cumsum()).cumcount()


logs.groupby("num").ne(logs.shift()).cumsum().groupby("num").size().max()


# def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
