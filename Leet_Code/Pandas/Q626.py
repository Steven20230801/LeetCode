import numpy as np
import pandas as pd


data = [[1, "Abbot"], [2, "Doris"], [3, "Emerson"], [4, "Green"], [5, "Jeames"]]
seat = pd.DataFrame(data, columns=["id", "student"]).astype(
    {"id": "Int64", "student": "object"}
)

test = (seat["id"] == len(seat)) & (seat["id"] % 2 == 1)

# change 1,2 3,4
seat["student"] = np.where(
    seat["id"] % 2 == 0,
    seat["student"].shift(1),
    # 若是最後一個且是奇數, 維持原樣
    np.where(
        (seat["id"] == len(seat)) & (seat["id"] % 2 == 1),
        seat["student"],
        seat["student"].shift(-1),
    ),
)
