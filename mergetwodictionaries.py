def merge_dicts(d1,d2):
    merged = d1.copy()
    merged.update(d2)
    return merged
dict1 = {"a":5, "b":7}
dict2 = {"b":9, "c":3}
print(merge_dicts(dict1,dict2))
