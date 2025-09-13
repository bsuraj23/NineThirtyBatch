list=[2,4,2,5,6,7,4]
unique=[]
for num in list:
    if num not in unique:
        unique.append(num)
print(unique)