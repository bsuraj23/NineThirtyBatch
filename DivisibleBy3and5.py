#printing numbers which are divisible by both 3 and 5 from 1 to 100 numbers
n=100
nums=[]
for i in range(1,n+1):
    if i%15==0:
        nums.append(i)
print(nums)