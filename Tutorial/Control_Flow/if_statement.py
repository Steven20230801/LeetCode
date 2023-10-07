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
