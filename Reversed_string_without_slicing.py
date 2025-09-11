""" REVERSING A STRING """
def reversed_string(s):
    reversed_str=""
    for char in s:
        reversed_str=char+reversed_str
    return reversed_str
print(reversed_string("abhishek"))