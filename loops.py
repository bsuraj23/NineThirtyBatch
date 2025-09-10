#loops are for,while
#for loop
n=10
for i in range(1,n):
    print(i)

fruits=["apple","orange","cherry","watermelon"]
for i in fruits:
    print(i)

#prime or not
num=23
if num>1:
    for i in range(2,num):
        if num % i==0:
            print("not a  prime")
            break
    else:
        print("prime")

#length of the list
li=[10,20,30]
count=0
for i in li:
    count+=i
print(count)

#even numbers print
e=20
for i in range(1,101):
    if(i%2==0):
        print(i)


#while loop
i=0
while i<5:
    print(i)
    i+=1
#sum of first 10 natural numbers
i=1
total=0
while i<=10:
    total+=i
    i+=1
    print(total)


