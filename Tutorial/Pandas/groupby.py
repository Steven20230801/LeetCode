import pandas as pd

data = {"category": ["A", "A", "B", "B", "C", "C"], "value": [1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(data)
df.head(10)

# sum
df.groupby("category").sum().reset_index()

# group by arrange

# first row of each group
df.sort_values("value", ascending=True).groupby("category").first().reset_index()
df.sort_values("value", ascending=False).groupby("category").first().reset_index()

# largest row of each group
df.sort_values("value", ascending=False).groupby("category").head(1).reset_index()

# smallest row of each group
df.sort_values("value", ascending=True).groupby("category").head(1).reset_index()
