#reverse a string
string="ammu"
rev=" "
for i in string:
    rev=i+rev
print(rev)


#Find the largest number in the list
num=[8,2,9,5,4]
print(max(num))


num=[10,2,3,4,676,9,789]
num.sort()
print(num[-1])

n=[1,3,4,76,4,67,8,90]
largest=n[0]
for i in n:
    if i>largest:
        largest=i
print(largest)


#count vowels in string
str="hello world"
vowels="aeiouAEIOU"
count=0
for i in str:
    if i in vowels:
        count+=1
print(count)


#check if prime or not
p=15
if p>1:
    for i in range (2,p):
        if p%i==0:
            print("non prime")
            break
    else:
        print("prime")


        


