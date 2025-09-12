#Reverse a string without using slicing
text = "Hello World"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text  

print("Original string:", text)
print("Reversed string:", reversed_text)