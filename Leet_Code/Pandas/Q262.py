import pandas as pd

data = [
    ["1", "1", "10", "1", "completed", "2013-10-01"],
    ["2", "2", "11", "1", "cancelled_by_driver", "2013-10-01"],
    ["3", "3", "12", "6", "completed", "2013-10-01"],
    ["4", "4", "13", "6", "cancelled_by_client", "2013-10-01"],
    ["5", "1", "10", "1", "completed", "2013-10-02"],
    ["6", "2", "11", "6", "completed", "2013-10-02"],
    ["7", "3", "12", "6", "completed", "2013-10-02"],
    ["8", "2", "12", "12", "completed", "2013-10-03"],
    ["9", "3", "10", "12", "completed", "2013-10-03"],
    ["10", "4", "13", "12", "cancelled_by_driver", "2013-10-03"],
]
trips = pd.DataFrame(
    data, columns=["id", "client_id", "driver_id", "city_id", "status", "request_at"]
).astype(
    {
        "id": "Int64",
        "client_id": "Int64",
        "driver_id": "Int64",
        "city_id": "Int64",
        "status": "object",
        "request_at": "object",
    }
)

data = [
    ["1", "No", "client"],
    ["2", "Yes", "client"],
    ["3", "No", "client"],
    ["4", "No", "client"],
    ["10", "No", "driver"],
    ["11", "No", "driver"],
    ["12", "No", "driver"],
    ["13", "No", "driver"],
]
users = pd.DataFrame(data, columns=["users_id", "banned", "role"]).astype(
    {"users_id": "Int64", "banned": "object", "role": "object"}
)

print(trips)
print(users)

df = trips.merge(users, left_on="client_id", right_on="users_id", how="left")
df = df.merge(users, left_on="driver_id", right_on="users_id", how="left")
print(df)
# 排除任一ban
df = df[~(df.banned_x.eq("Yes") | df.banned_y.eq("Yes"))]
# 排除非10-01 ~ 10-03
df = df[df.request_at.between("2013-10-01", "2013-10-03")]
# group by request_at 計算總數 & 計算status 字段代cancel的數量
df = (
    df.groupby("request_at")
    .agg(
        trips_count=("id", "count"),
        cancel_count=("status", lambda x: x.str.contains("cancel").sum()),
    )
    .reset_index()
)
df["cancel_rate"] = (df["cancel_count"] / df["trips_count"]).round(2)
print(df)
