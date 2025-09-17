# reverse of a string
"""def reverse_string(text):
    rev = ""
    for char in text:
        rev = char + rev
    return rev

print("Reversed:", reverse_string("Python"))"""


def reverse(text):
    if text==0:
        return text
    else:
        return text[::-1] 
print("Reverse",reverse("python"))    

