def my_max(numbers):
    if not numbers:
        raise ValueError("my_max() arg is an empty sequence")
    
    maximum = numbers[0]
    
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
            
    return maximum
nums = [3, 7, 2, 9, 5]
print(my_max(nums))  
