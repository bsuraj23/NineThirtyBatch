# control statements-if,ifelse,elif,nestedif
# if 
a=45
if(a>0):
    print("positive")

#if else (find greater one)
a=10
b=2
if(a>b):
    print("a is the greater one",a)
else:
    print("b is the greater one",b)

#even or odd
n=26
if(n %2==0):
    print("even number")
else:
    print("odd number")

#eligible to vote
a=12
if(a>=18):
    print("eligible to vote")
else:
    print("not eligible to vote")


#elif statement
#whether the number is positive or negative
x=-56
if(x>0):
    print("positive")
elif(x==0):
    print("zero")
else:
    print("negative")

#big among three values
a=10
b=4
c=-3
if(a>b)&(a>c):
    print(a)
elif(b>a)&(b>c):
    print(b)
else:
    print(c)

#leap year
year=2002
if(year%400==0)&(year%100==0):
    print("leap year")
elif(year%4==0)&(year%100!=0):
    print("leap year")
else:
    print("non leap year")


#grades
marks=78
if(marks>=90):
    print("A grade")
elif(marks>=70):
    print("B grade")
elif(marks>=35):
    print("c grade")
else:
    print("fail")

#nested if 
num=-5
if num>=0:
    if num==0:
        print("zero")
    else:
        print("positive")
else:
    print("negative")