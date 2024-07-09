p = (4, 5)
x, y = p
print(f"x: {x}, y: {y}")
# 前提是tuple的長度和變數的數量要一樣

try:
    data = ["ACME", 50, 91.1, (2012, 12, 21)]
    name, shares, price = data
except ValueError as e:
    print(e)


name, shares, price, date = data
print(f"name: {name}, shares: {shares}, price: {price}, date: {date}")

