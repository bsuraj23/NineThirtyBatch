my_list = [50, 10, 30, 20, 40]       # Our initial list

# Append → add an element at the end
my_list.append(60)                     # adds 60 at the end
print(my_list)                         # [50, 10, 30, 20, 40, 60]

# Insert → add an element at a specific index
my_list.insert(2, 25)                  # insert 25 at index 2
print(my_list)                         # [50, 10, 25, 30, 20, 40, 60]

# Remove → remove first occurrence of a value
my_list.remove(20)                     # removes 20
print(my_list)                         # [50, 10, 25, 30, 40, 60]

# Pop → remove element at specific index (default is last)
my_list.pop(1)                         # removes element at index 1 (10)
print(my_list)                         # [50, 25, 30, 40, 60]

# Sort → sort list in ascending order
my_list.sort()                         # sorts list
print(my_list)                         # [25, 30, 40, 50, 60]

# Reverse → reverse the order of elements
my_list.reverse()                      # reverses list
print(my_list)                         # [60, 50, 40, 30, 25]
