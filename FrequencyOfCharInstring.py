sentence= input("Enter a string: ")

freq = {}
for char in sentence:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character frequencies:")
for key, value in freq.items():
    print(f"{key} : {value}")
