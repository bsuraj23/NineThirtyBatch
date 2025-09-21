def sum_of_digits(n):
    total = 0
    for digit in str(abs(n)):  # convert to string & handle negatives
        total += int(digit)
    return total

# Example usage
print(sum_of_digits(12345))   # 15
print(sum_of_digits(-987))    # 24
