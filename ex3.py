def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Call the function and print the result
text = "this was simple as starting a car"
print(count_vowels(text))