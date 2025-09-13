my_tuple = (10, 20, 30, 20, 40, 20)   # Creating a tuple with repeated elements

# count() → counts how many times a value appears in the tuple
print(my_tuple.count(20))  # 3 → 20 appears 3 times in the tuple

# index() → returns the index of the first occurrence of a value
print(my_tuple.index(30))  # 2 → 30 is first found at index 2
print(my_tuple.index(20))  # 1 → first occurrence of 20 is at index 1
