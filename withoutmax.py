def my_max(iterable):
    if not iterable:
        raise ValueError("my_max() is empty")
    maximum = iterable[0]
    for item in iterable[1:]:
        if item > maximum:
         maximum = item
    return maximum
print(my_max([1,2,5,8,4]))