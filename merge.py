def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()  # Start with a copy of the first dictionary
    merged.update(dict2)   # Update with the second dictionary
    return merged
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = merge_dictionaries(dict1, dict2)
print(merged_dict)
# Output: {'a': 1, 'b': 3, 'c': 4}
