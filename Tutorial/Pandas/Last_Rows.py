import pandas as pd

# Create a DataFrame
data = {"group_column": ["A", "A", "B", "B", "C"], "value_column": [1, 2, 3, 4, 5]}

df = pd.DataFrame(data)

# last rows
df_last = df.tail(1)

# Group by 'group_column' and retain the last row in each group
result_df = df.groupby("group_column").last().reset_index()

# Print the result
print(result_df)
