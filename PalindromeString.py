sentence=input("Enter a sentence: ")
empty=""
for i in sentence:
    empty=i+empty
if sentence==empty:
        print("The string is palindrome")
else:
        print("The string is not palindrome") 