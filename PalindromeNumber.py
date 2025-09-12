num=input("Enter a number: ")
empty=""
for i in num:
    empty=i+empty
if num==empty:
        print("The number is palindrome")
else:
        print("The number is not palindrome") 