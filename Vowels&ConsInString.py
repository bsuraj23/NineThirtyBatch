sentence=input("Enter a Sentence: ")
vow=0
cons=0
vowels="aeiouAEIOU"
consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
for char in sentence:
    if char in vowels:
        vow+=1
    elif char in consonants:
        cons+=1
print("The conunt of vowels is: ",vow)
print("The count of consonants is: ",cons)


