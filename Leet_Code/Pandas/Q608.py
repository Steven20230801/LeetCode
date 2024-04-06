import numpy as np
import pandas as pd

data = [[1, None], [2, 1], [3, 1], [4, 2], [5, 2]]
tree = pd.DataFrame(data, columns=["id", "p_id"]).astype(
    {"id": "Int64", "p_id": "Int64"}
)

tree

# id 如果不再P_id裡面，就是root
# id 如果在P_id裡面，但是P_id不在id裡面，就是leaf
# id 如果在P_id裡面，但是P_id也在id裡面，就是middle
tree["type"] = np.where(
    tree["id"].isin(tree["p_id"]),
    np.where(tree["p_id"].isin(tree["id"]), "Inner", "Root"),
    "Leaf",
)

len(tree)


def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree["type"] = np.where(
        tree["id"].isin(tree["p_id"]),
        np.where(tree["p_id"].isin(tree["id"]), "Inner", "Root"),
        "Leaf",
    )

    return tree[["id", "type"]]
