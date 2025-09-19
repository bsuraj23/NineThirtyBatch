def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage:
input_string = "Hello, how are you?"
print("Number of vowels:", count_vowels(input_string))