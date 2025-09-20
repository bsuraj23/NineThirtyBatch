def second_largest(nums):
    if len(nums) < 2:
        return None  # Not enough elements

    largest = second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    return second if second != float('-inf') else None
print(second_largest([10, 20, 4, 45, 99]))   # Output: 45
print(second_largest([5, 5, 5]))             # Output: None (no second largest)
