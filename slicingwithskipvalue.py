text = "amazing"                 # Our string

print(text[0:7:2])  # "aai" → from index 0 to 6, skipping every 2nd character
print(text[1:7:2])  # "mzn" → from index 1 to 6, skipping every 2nd character
print(text[::3])    # "ai"  → whole string, pick every 3rd character
print(text[::-1])   # "gnizama" → reverse the string (step = -1)
print(text[::-2])   # "giaa" → reverse string and skip every 2nd character
