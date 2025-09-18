# Find largest number in a list
def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

# Example
numbers = [10, 45, 67, 23, 89, 12]
print("List:", numbers)
print("Largest number:", find_largest(numbers))