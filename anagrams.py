def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
