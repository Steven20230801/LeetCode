# Define a function to square a number
def square(x):
    return x**2


# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the map function to apply the square function to each element in the list
squared_numbers = map(square, numbers)
print(type(squared_numbers))

# Convert the map object to a list
squared_numbers = list(squared_numbers)

# Print the squared numbers
print(squared_numbers)


dic = {1: 2, 3: 4, 5: 6}
print(dic)


import pandas as pd

# pandas map
# Create a DataFrame
data = {"A": [1, 2, 3, 4, 5], "B": [2, 3, 4, 5, 6]}
df = pd.DataFrame(data)
df["A_squared"] = df["A"].map(square)
print(df)
