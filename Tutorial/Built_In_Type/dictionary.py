# dictionary basic intro
# dictionary is mutable
# dictionary is unordered
# dictionary is indexed

dictionary_a = {}
dictionary_a = dict()
dictionary_a = {"a": 1, "b": 2}
dictionary_a = dict(a=5, b=2)
print(f"dictionary_a: ", dictionary_a)
# insert/ update
dictionary_a["a"] = 1
print(f"dictionary_a: ", dictionary_a)
dictionary_a["b"] = 2
# method
dictionary_a.update({"c": 3, "d": 4})
print(f"dictionary_a: ", dictionary_a)
dictionary_a.pop("a")
print(f"dictionary_a: ", dictionary_a)
dictionary_a.popitem()
print(f"dictionary_a: ", dictionary_a)
dictionary_a.clear()
print(f"dictionary_a: ", dictionary_a)

dictionary_a = {"a": 1, "b": 2}
dictionary_a.setdefault("a", "None")
test = print(dictionary_a.get("c"))  #  dictionary_a.get("c")
dictionary_a.setdefault("c", "None123")

dictionary_a.__len__()
len(dictionary_a)

str(dictionary_a)
dictionary_a.__str__()

# key
dictionary_a.keys()
# loop
for key in dictionary_a.keys():
    print(f"key: {key}")
# value
dictionary_a.values()
# loop
for value in dictionary_a.values():
    print(f"value: {value}")


# items
dictionary_a = {"a": 1, "b": 2}
print(f"dictionary_a.items(): ", dictionary_a.items())
# loop
for key, value in dictionary_a.items():
    print(f"key: {key}, value: {value}")
