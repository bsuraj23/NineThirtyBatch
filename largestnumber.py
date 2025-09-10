numbers = [3, 7, 2, 9, 5]
largest = numbers[0]  

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)