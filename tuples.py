# Tuples in Python

# Creating a tuple
my_tuple = (10, 20, 30, "hello", 3.14, True)

print("Tuple:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])      # 10
print("Last element:", my_tuple[-1])      # True

# Slicing a tuple
print("Slice [1:4]:", my_tuple[1:4])      # (20, 30, 'hello')

# Tuple is immutable, so you cannot change its elements
# my_tuple[0] = 99  # This will raise an error

# Tuple with only one element need a comma)
single_element_tuple = (5,)
print("Single element tuple:", single_element_tuple)