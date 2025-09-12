# String Functions in Python

text = "Hello, welcome to Python programming. Python is fun!"

# len() function - returns the length of the string
print("Length of text:", len(text))  # 52

# endswith() function - checks if the string ends with a specified suffix
print("Ends with 'fun!':", text.endswith("fun!"))  # True

# count() function - counts occurrences of a substring
print("Count of 'Python':", text.count("Python"))  # 2

# Accessing the first character of the string
print("First character:", text[0])  # 'H'

# find() function - returns the index of the first occurrence of a substring
print("Index of 'welcome':", text.find("welcome"))  # 7