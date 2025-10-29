n=input("enter a string")
rev=" "
for i in n:
    rev=i+rev
if n==rev:
    print(n,"is palindrome")   
print(n,"is not palindrome")
