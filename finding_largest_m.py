def finding_largest(s):
    largest=s[0]
    for num in s:
        if num>largest:
            largest=num
    return largest
print(finding_largest([12,45,74,88,34,56]))
