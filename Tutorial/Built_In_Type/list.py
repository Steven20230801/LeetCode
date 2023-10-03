list_x = list(range(1, 6))  # [1, 2, 3, 4, 5]
list_x = [1, 2, 3, 4, 5, 1]
# index = 0, 1, 2, 3, 4, 5

print(f"list_x : {list_x}")
print(f"list_x[0] : {list_x[0]}")  # x in s

# find first index of x in s
print(f"list_x.index(1) : {list_x.index(1)}")

# raise ValueError if x not in s
# print(f"list_x.index(6) : {list_x.index(6)}")

# mutable sequence type opreations
# s[i] = x
list_x[0] = 6
print(f"list_x : {list_x}")

# del s[i]
del list_x[0]
print(f"list_x : {list_x}")

# s[i:j] = t
list_x[0:2] = [6, 7]
print(f"list_x : {list_x}")

# del s[i:j]
del list_x[0:2]
print(f"list_x : {list_x}")

# s[i:j:k] = t
list_x[0:3:2] = [6, 7]
print(f"list_x : {list_x}")

# del s[i:j:k]

# s.append(x)
list_x.append(6)
print(f"list_x : {list_x}")

# s.clear()
list_x.clear()
print(f"list_x : {list_x}")

# s.copy()
list_x = list(range(1, 6))
list_y = list_x.copy()
print(f"list_x : {list_x}")
print(f"list_y : {list_y}")

# s.extend(t)
list_x.extend([6, 7, 8])
print(f"list_x : {list_x}")

# s *= n
list_x *= 2
print(f"list_x : {list_x}")

# s.insert(i, x)
list_x.insert(0, 0)
print(f"list_x : {list_x}")

# s.pop([i])
list_x.pop(0)
print(f"list_x : {list_x}")

# s.remove(x)
list_x.remove(1)
print(f"list_x : {list_x}")

# s.reverse()
list_x.reverse()
print(f"list_x : {list_x}")

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
