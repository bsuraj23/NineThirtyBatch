<<<<<<< HEAD
#finding frequency of string

sentence="find the frequency of each character in string"
freq={}

for char in sentence:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
=======
#finding frequency of string

sentence="find the frequency of each character in string"
freq={}

for char in sentence:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
>>>>>>> 5e604e6 ( Added Some more programs)
print(freq)