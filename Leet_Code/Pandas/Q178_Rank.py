import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(by="score", ascending=False)
    scores["rank"] = (
        scores["score"].rank(method="dense", ascending=False).astype("Int64")
    )
    return scores[["score", "rank"]]


if __name__ == "__main__":
    data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
    scores = pd.DataFrame(data, columns=["id", "score"]).astype(
        {"id": "Int64", "score": "Float64"}
    )
    print(order_scores(scores))
