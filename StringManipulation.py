#Function for Remove all vowels in a given String
def remove_vowels(s):
    vowels="aeiouAEIOU"
    result=[]
    for ch in s:
        if ch not in vowels:
            result.append(ch)
    return ''.join(result)
print(remove_vowels("Akhila"))

#Frequency of each character in a given String
def char_freq(S):
    freq={}
    for ch in S:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq
print(char_freq("mynameisakhila"))

#Returns all substrings of length k
def substring_length(s,k):
    result=[]
    n=len(s)
    for i in range(n-k+1):
        substring=s[i:i+k]
        result.append(substring)
    return result
print(substring_length("Hello",2))

#combined all above functions
text="Hello World"
no_vowels=remove_vowels(text)
print("Without vowels:",no_vowels)
print("Character frequency:",char_freq(text))
print("Substrings of length 5:",substring_length(text,5))