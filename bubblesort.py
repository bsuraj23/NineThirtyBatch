temp=[22,7,4,17,19,89,9,11,16,55]
n=len(temp)-1
for i in range(n):
  for j in range(0,n-i):
        if temp[j]>temp[j+1]:
            temp[j],temp[j+1]=temp[j+1],temp[j]
print("SORTED LIST IS:",temp)