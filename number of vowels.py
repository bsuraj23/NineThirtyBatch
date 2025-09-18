# Count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example
text = "python batch"
print("String:", text)
print("Number of vowels:", count_vowels(text))