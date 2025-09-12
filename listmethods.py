# List Methods in Python

my_list = [5, 2, 9, 1]

my_list.append(7)         # Adds 7 at the end
print("After append:", my_list)

my_list.insert(2, 10)     # Inserts 10 at index 2
print("After insert:", my_list)

my_list.remove(2)         # Removes the first occurrence of 2
print("After remove:", my_list)

popped = my_list.pop()    # Removes and returns the last element
print("After pop:", my_list)
print("Popped element:", popped)

my_list.sort()            # Sorts the list in ascending order
print("After sort:", my_list)

my_list.reverse()         # Reverses the list
print("After reverse:", my_list)

index = my_list.index(9)  # Returns the index of first occurrence of 9
print("Index of 9:", index)

count = my_list.count(1)  # Counts how many times 1 appears
print("Count of 1:", count)

my_list.clear()           # Removes all elements from the list