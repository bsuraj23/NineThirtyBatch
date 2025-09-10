s =input("Enter a string : ")
rev = ""
for char in s:
    rev = char + rev
print(rev)  
print("Reversed string is:", rev)