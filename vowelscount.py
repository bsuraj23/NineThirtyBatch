def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for word in s:
        if word in vowels:
            count += 1
    return count

text = "What is Python"
print("Number of vowels:", count_vowels(text))