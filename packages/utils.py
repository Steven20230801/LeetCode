def flatten(x: list, drop_duplicates=True):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, str):
            result.extend(flatten(el))
        else:
            result.append(el)

    if drop_duplicates:
        result = list(set(result))

    return result
