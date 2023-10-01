import pandas as pd

# Sample DataFrame
data = {"Category": ["A", "B", "A", "C", "B", "A", "C", "C", "B", "A"]}
df = pd.DataFrame(data)
df["most_common"] = df["Category"].value_counts().head().index[0]
df["most_common2"] = df["Category"].mode()[0]
print(df)
# Use value_counts to count unique values and head to get the most common ones
most_common = df["Category"].value_counts().head()
most_common_dict = df["Category"].value_counts().head().to_dict()

print(most_common)
print(most_common_dict)
