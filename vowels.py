def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

# Test it
string = "Hello, how are you?"
print("Number of vowels:", count_vowels(string))