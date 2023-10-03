# set basic
# set is mutable
# set is unordered
# set is unindexed
# set is faster than list
# set can be used as key in dictionary
set_a = set()
set_a.add(1)
set_a.add(2)
set_a.add(1)
print(f"set_a: ", set_a)
set_a.remove(1)

# set from list
list_a = [1, 2, 3, 4, 5]
set_a = set(list_a)
print(f"set_a: ", set_a)

# set from tuple
tuple_a = (1, 2, 3, 4, 5, 2, 4)
set_a = set(tuple_a)
print(f"set_a: ", set_a)
