numbers = [4, 7, 2, 9, 5]
largest_number = numbers[0]  # Assume the first element is the largest
for number in numbers:
    if number > largest_number:
        largest_number = number

print(largest_number)
