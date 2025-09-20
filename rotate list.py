def rotate_right(lst, k):
    n = len(lst)
    k = k % n   # handle k > n
    return lst[-k:] + lst[:-k]
nums = [1, 2, 3, 4, 5]
print(rotate_right(nums, 2))   # [4, 5, 1, 2, 3]
