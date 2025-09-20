def flatten_list(nested_list):
    flat = []
    for sublist in nested_list:
        for item in sublist:
            flat.append(item)
    return flat
nums = [[1, 2], [3, 4], [5, 6]]
print(flatten_list(nums))   # Output: [1, 2, 3, 4, 5, 6]
