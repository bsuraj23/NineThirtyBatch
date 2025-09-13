text = "Farhan is amazing"              # Our string
print(len(text))          # 17 → length() function gives total characters in string

print(text.endswith("ing"))   # True → checks if string ends with "ing"
print(text.endswith("han"))   # False → string does not end with "han"

print(text.count("a"))    # 3 → counts how many times 'a' appears
print(text.count("an"))   # 2 → counts how many times "an" appears

print(text.find("is"))    # 7 → gives index of first occurrence of "is"
print(text.find("z"))     # -1 → returns -1 if not found

print(text.replace("amazing", "smart"))  # "Farhan is smart" → replaces word
