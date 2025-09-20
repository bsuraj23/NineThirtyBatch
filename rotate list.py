def my_max(iterable):
    if not iterable:
        raise ValueError("my_max() arg is an empty sequence")
    
    maximum = iterable[0]
    for item in iterable[1:]:
        if item > maximum:
            maximum = item
    return maximum
nums = [3, 7, 2, 9, 5]
print(my_max(nums))   # Output: 9

chars = ['a', 'x', 'd']
print(my_max(chars))  # Output: x
