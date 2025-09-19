def remove_duplicates(numbers):
    unique_numbers = []
    
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    
    return unique_numbers
numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]
print(remove_duplicates(numbers))
# Output: [1, 2, 3, 4, 5, 6]
