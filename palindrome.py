# string is palindrome or not

word=input("enter a string:")
if list(word)==list(reversed(word)):
    print("it is palindrome")
else:
    print("not a palindrome")
