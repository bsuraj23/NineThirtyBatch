#counting vowels in a string

message = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in message:
    if char in vowels:
        count += 1

print("Number of vowels:", count)