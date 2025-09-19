def char_frequency(s):
    frequency = {}
    
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    return frequency
text = "hello world"
freq = char_frequency(text)
print(freq)
