# dictionary basic intro
# dictionary is mutable
# dictionary is unordered
# dictionary is indexed

dictionary_a = {}
dictionary_a["a"] = 1
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
