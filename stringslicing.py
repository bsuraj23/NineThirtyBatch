# String Slicing in Python

text = "Farhan"

print(text[0:3])    # 'Far' - characters from index 0 to 2
print(text[2:])     # 'rhan' - from index 2 to end
print(text[:4])     # 'Farh' - from start to index 3
print(text[-3:])    # 'han' - last 3 characters
print(text[::2])    # 'Frh' - every second character
print(text[::-1])   # 'nahraF' - reversed string