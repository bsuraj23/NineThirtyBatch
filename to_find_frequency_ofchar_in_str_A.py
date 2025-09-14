def freq_char(str):
    frequency={}
    for char in str:
        if char in frequency:
            frequency[char]=frequency[char]+1
        else:
            frequency[char]=1
    return frequency
print(freq_char("My Name Is Abhishek"))