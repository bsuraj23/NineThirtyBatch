def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev   # add each character in front
    return rev

# Example
string = "python"
print("Original:", string)
print("Reversed:", reverse_string(string))