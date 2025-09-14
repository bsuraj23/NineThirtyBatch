def my_max(iterable):
    iterator=iter(iterable)
    try:
        current_max=next(iterator)
    except StopIteration:
        raise ValueError("my_max is an empty iterable")
    for item in iterator:
        if item>current_max:
            current_max=item
    return current_max
print(my_max([2,4,3,11]))
print(my_max("abhishek"))
print(my_max((-10,-20,-6)))
# print(my_max(()))