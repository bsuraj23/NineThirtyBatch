
text = "keywords are reversed"

vowels = "aeiouAEIOU"  
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)