def counting_vowelsandconsonants(str):
    vowels=set("aeiouAEIOU")
    vowel_count=0
    consonant_count=0
    for char in str:
        if char.isalpha():
            if char in vowels:
                vowel_count=vowel_count+1
            else:
                consonant_count=consonant_count+1
    return vowel_count,consonant_count
str="welcome to python code"
v,c=counting_vowelsandconsonants(str)
print("vowels:",v,"consonants:",c)