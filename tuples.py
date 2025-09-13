# A tuple is an ordered, immutable collection of elements in Python
# Tuples can hold elements of different data types (int, float, string, etc.)

my_tuple = (10, 3.14, "Farhan", True, None, 'A')   # Creating a tuple with multiple data types

print(my_tuple)           # (10, 3.14, 'Farhan', True, None, 'A') → prints the whole tuple
print(my_tuple[0])        # 10 → first element (integer)
print(my_tuple[1])        # 3.14 → second element (float)
print(my_tuple[2])        # Farhan → third element (string)
print(my_tuple[-1])       # 'A' → last element (character)

# Tuple can also contain another tuple (nested tuple)
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple)       # (1, 2, (3, 4), 5)
print(nested_tuple[2])    # (3, 4) → accessing the nested tuple
print(nested_tuple[2][0]) # 3 → accessing element inside the nested tuple
