print("reverse")
def reversed_string(s):
    reversed_str=""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
text="hello"
print("reversed string",reversed_string(text))


