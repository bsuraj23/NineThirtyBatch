n=int(input("enter a number"))
if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")


# greatest number in three numbers
a=int(input("enter first number"))
b=int(input("enter second number")) 
c=int(input("enter third number"))
if a>=b and a>=c:
    print(a,"is greatest")
elif b>=a and b>=c:
    print(b,"is greatest")
else:
    print(c,"is greatest")


# factorial of a number
num=int(input("enter a number"))
factorial=1 
for i in range(1,num+1):
    factorial=factorial*i
print("factorial of",num,"is",factorial)



