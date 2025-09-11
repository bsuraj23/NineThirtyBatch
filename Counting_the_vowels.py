def counting_vowels(str):
    vowels="aeiouAEIOU"
    count=0
    for char in str:
        if char in vowels:
            count=count+1
    return count
print(counting_vowels("Abhishek"))