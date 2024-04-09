import pandas as pd

data = [
    [121, "US", "approved", 1000, "2018-12-18"],
    [122, "US", "declined", 2000, "2018-12-19"],
    [123, "US", "approved", 2000, "2019-01-01"],
    [124, "DE", "approved", 2000, "2019-01-07"],
]
transactions = pd.DataFrame(
    data, columns=["id", "country", "state", "amount", "trans_date"]
).astype(
    {
        "id": "Int64",
        "country": "object",
        "state": "object",
        "amount": "Int64",
        "trans_date": "datetime64[ns]",
    }
)

print(transactions)
# group by country and month
transactions["month"] = transactions["trans_date"].dt.to_period("M")


df = (
    transactions.groupby(["month", "country"])
    .agg(
        **{
            "trans_count": ("id", "count"),
            "approved_count": ("state", lambda x: (x == "approved").sum()),
            "trans_total_amount": ("amount", "sum"),
            "trans_approved_amount": (
                "amount",
                lambda x: x[transactions["state"] == "approved"].sum(),
            ),
        }
    )
    .reset_index()
)

print(df)


def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    # 確保 trans_date 是日期時間類型
    transactions["trans_date"] = pd.to_datetime(transactions["trans_date"])
    transactions["month"] = transactions["trans_date"].dt.strftime("%Y-%m")

    # 首先篩選出核准的交易，這樣在計算核准相關的統計時可以提高效率
    approved_transactions = transactions[transactions["state"] == "approved"]

    # 使用 groupby 和 agg 進行分組和聚合
    df = (
        transactions.groupby(["month", "country"])
        .agg(
            trans_count=("id", "count"),
            trans_total_amount=("amount", "sum"),
        )
        .reset_index()
    )

    # 分別對核准的交易進行聚合計算
    approved_df = (
        approved_transactions.groupby(["month", "country"])
        .agg(
            approved_count=("id", "count"),
            trans_approved_amount=("amount", "sum"),
        )
        .reset_index()
    )

    # 將核准的統計數據合併到主 DataFrame
    df = pd.merge(df, approved_df, on=["month", "country"], how="left")

    # 將缺失值填充為0，因為可能有些組合沒有核准的交易
    df.fillna({"approved_count": 0, "trans_approved_amount": 0}, inplace=True)

    return df


monthly_transactions(transactions)


def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["approved"] = np.where(
        transactions["state"] == "approved", transactions["amount"], np.nan
    )
    transactions["month"] = transactions["trans_date"].dt.strftime("%Y-%m")
    return (
        transactions.groupby(["month", "country"], dropna=False)
        .agg(
            trans_count=("state", "count"),
            approved_count=("approved", "count"),
            trans_total_amount=("amount", "sum"),
            approved_total_amount=("approved", "sum"),
        )
        .reset_index()
    )
