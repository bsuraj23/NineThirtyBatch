def reverse_list(nums: list) -> None:
    left, right = 0, len(nums) - 1
    while left < right:
        # Swap elements
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# Example usage
numbers = [1, 2, 3, 4, 5]
reverse_list(numbers)
print(numbers)   # [5, 4, 3, 2, 1]