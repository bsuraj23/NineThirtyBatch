def finding_largest(s):
    largest=s[0]
    for num in s:
        if num>largest:
            largest=num
    return largest
print(finding_largest([12,71,91,26,63,112,56,43]))