# if basic
# if can be used as expression
# if can be used as statement
# if can be used as statement block
# if can be used as statement block with else

x = 1

if x == 1:
    print("x == 1")
else:
    print("x != 1")

# if can be used as statement block with elif
if x == 1:
    print("x == 1")
elif x == 2:
    print("x == 2")
else:
    print("x != 1 and x != 2")

# False value
# False
# None
# 0
# 0.0
# 0j
# Decimal(0)
# Fraction(0, 1)
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# '' - an empty str
# b'' - an empty bytes
# set() - an empty set
# an empty range, like range(0)
# objects for which
# obj.__bool__() returns False
# obj.__len__() returns 0

x = ""
if x:
    print("x is not empty")
else:
    print("x value is empty")

# and
a = 1 and 2 and 3
print(a)  # last True value
b = 1 and 0 and 3
print(b)  # 0, first False value
# or
a = 1 or 2 or 3
print(a)  # first True value
b = 0 or 0 or 3
print(b)  # first True value
# not
a = not 1
print(a)  # False
b = not 0
print(b)  # True

x = 100
if x > 0 and x < 100:
    print("x > 0 and x < 100")
elif x >= 100 and x < 200:
    print("x > 100 and x < 200")
else:
    print("x > 200")
