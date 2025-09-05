#airthmatic operators
a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)

#relational operators
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
print(b!=a)

#assignment operators
a1=10
print(a)
a1+=2
print(a1)
a1-=3
print(a1)
a1*=2
print(a1)
a1/=2
print(a1)
a1//=3
print(a1)
a1**=2
print(a1)

#logical operators
b=10
c=20
print(b>c and b<c)
print(b==c and b>c)
print(b<=c or b>=c)
print(not b<c)
print(not c>b)

#bitwise operators
s=2
m=4
print (s & m)
print(s | b)
print(s ^ m)
print(~s)
print(~m)
print(s<<1)
print(s>>1)
print(m<<1)
print(m>>1)

#membership operators
f=[1,2,3,4,5,6,7,8,9]
print( 2 in f)
print(7 not in f)
word="python"
print('p' in word)
print('z' not in word)
print('y' not in word)

#identity operator
i1=[1,2,3,4]
i2=[1,2,3,4,5,6]
print (i1 is i2)
print(i2 is i1)
print(i1 is not i2)
print(i2 is not i1)