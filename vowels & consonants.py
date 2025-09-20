def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    
    for char in text:
        if char.isalpha():  # consider only letters
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    
    return v_count, c_count
s = "Hello World"
v, c = count_vowels_consonants(s)
print("Vowels:", v)       # 3 (e, o, o)
print("Consonants:", c)   # 7 (H, l, l, W, r, l, d)
