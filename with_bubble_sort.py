temp=[2,4,74,44,999,82,99,56]
n=len(temp)-1
for i in range(n):
    for j in range(0,n-i):
        if temp[j]>temp[j+1]:
            temp[j],temp[j+1]=temp[j+1],temp[j]
            i=i+1
print(temp)