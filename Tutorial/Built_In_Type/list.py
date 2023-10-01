list_x = list(range(1, 6))  # [1, 2, 3, 4, 5]
list_x = [1, 2, 3, 4, 5, 1]
# index = 0, 1, 2, 3, 4, 5

print(f"list_x : {list_x}")
print(f"list_x[0] : {list_x[0]}")  # x in s

# find first index of x in s
print(f"list_x.index(1) : {list_x.index(1)}")

# raise ValueError if x not in s
# print(f"list_x.index(6) : {list_x.index(6)}")

# x in s
print(f"1 in list_x : {1 in list_x}")
print(f"6 in list_x : {6 in list_x}")


# x not in s
print(f"1 not in list_x : {1 not in list_x}")
print(f"6 not in list_x : {6 not in list_x}")

# s + t
list_y = [6, 7, 8, 9, 10]
print(f"list_x + list_y : {list_x + list_y}")

# s * n
print(f"list_x * 3 : {list_x * 3}")

# len(s)
print(f"len(list_x) : {len(list_x)}")

# min(s)
print(f"min(list_x) : {min(list_x)}")

# list_x = [1, 2, 3, 4, 5, "abc"]
# print(f"min(list_x) : {min(list_x)}")

# max(s)
print(f"max(list_x) : {max(list_x)}")


# list method
list_x = list()
list_x = []

# append
list_x.append(1)
list_x.append(2)

# extend
list_x.extend([3, 4, 5])

# insert
list_x.insert(0, 0)
list_x.insert(6, 6)

# remove
print(f"before remove : {list_x}")
list_x.remove(6)
print(f"after remove : {list_x}")

# 2 element in list
list_x.insert(1, 6)
list_x.insert(5, 6)
print(f"before remove : {list_x}")
list_x.remove(6)
print(f"after remove : {list_x}")
