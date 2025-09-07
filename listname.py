# ✅ List Creation
empty_list = []
print("Empty list:", empty_list)
print("Type:", type(empty_list))

# ✅ Indexing
numbers = [1, 2, 3, 4, 5]
print("First element:", numbers[0])

Names = ["Tanjiro", "Gojo", "Eren", "Luffy"]
print("First Name:", Names[0])
print("Last Name:", Names[-1])

# ✅ Mixed Data Types
mixed = [1, "bye", 3.14, True]
print("Mixed list:", mixed)

# ✅ List Methods

# 🔹 append() – Adds one item to the end
Names.append("Johan")
print("After append:", Names)

# 🔹 extend() – Adds multiple items
Names.extend(["Light", "Isagi"])
print("After extend:", Names)

# 🔹 insert() – Inserts at specific index
Names.insert(2, "Naruto")
print("After insert:", Names)

# 🔹 remove() – Removes first occurrence of value
Names.remove("Luffy")
print("After remove:", Names)

# 🔹 pop() – Removes by index (default: last)
popped_item = Names.pop()
print("Popped item:", popped_item)
print("After pop:", Names)

# 🔹 clear() – Empties the list
temp = [1, 2, 3]
temp.clear()
print("After clear:", temp)

# 🔹 index() – Finds first index of value
nums = [10, 20, 30, 20, 40]
print("Index of 20:", nums.index(20))
print("Index of 20 after index 2:", nums.index(20, 2))

# 🔹 count() – Counts occurrences
print("Count of 20:", nums.count(20))

# 🔹 sort() – Sorts in ascending order
unsorted = [5, 3, 8, 1, 9]
unsorted.sort()
print("Sorted list:", unsorted)

# 🔹 reverse() – Reverses the list
unsorted.reverse()
print("Reversed list:", unsorted)

# 🔹 copy() – Creates a shallow copy
copied = Names.copy()
print("Copied list:", copied)