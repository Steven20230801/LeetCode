import pandas as pd

data = [[1, "Joe"], [2, "Henry"], [3, "Sam"], [4, "Max"]]
customers = pd.DataFrame(data, columns=["id", "name"]).astype(
    {"id": "Int64", "name": "object"}
)
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=["id", "customerId"]).astype(
    {"id": "Int64", "customerId": "Int64"}
)

print(customers)
print(orders)

df = customers.merge(orders, left_on="id", right_on="customerId", how="left")
df[df.id_y.isnull()][["name"]].rename(columns={"name": "Customers"})
