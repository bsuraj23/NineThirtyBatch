#numeric types(int,float,complex)
#integer
a=10
print(type(a))
#float
b=10.5
print(type(b))
#complex
c=3+5j
print(type(c))
d=2+0j
print(type(d))

#sequence data types(str,list,tuple)
#string
str='hello!,we are from medha edu tech'
print(str)
print(type(str))
str1="Hello python"
print(str1)
print(type(str1))
str2='''hello python'''
print(str2)
print(type(str2))
str3=""" hello python"""
print(str3)
print(type(str3))
str4=''
print(type(str4))
str5=" "
print(str5)
print(type(str5))


#list
li1=[1,2,3,4,5]
print(li1)
print(type(li1))
li2=["apple","banana","orange","cherry","apple"]
print(li2)
print(type(li2))
li3=[1,2,3,"apple","cherry",10.5,3.167,True]
print(li3)
print(type(li3))
li4=[]
print(li4)
print(type(li4))


#Tuple
t1=(1,2,3,4,5)
print(t1)
print(type(t1))
t2=('apple','orange','cherry')
print(t2)
print(type(t2))
t3=('ammu',1,2,3,4,12.3,True,False,"ammulu")
print(t3)
print(type(t3))
t4=()
print(type(t4))

#set types(set,frozenset)
s1={1,2,3,4,5}
print(s1)
print(type(s1))
s2={1,2,3,"ammu","apple"}
print(type(s2))
s3={}
print(s3)
print(type(s3))
#frozenset
fs=frozenset([10,20,30,40])
print(fs)
print(type(fs))

#mapping type(dictionary)
d1={1:"apple",2:"banana",3:"cherry"}
print(d1)
print(d1.keys())
print(d1.values())
print(type(d1))
d2={1:1,2:3.333,3:"ammu",4:True,5:[1,2,3,4]}
print(d2)
print(d2.keys())
print(d2.values())
print(type(d2))

#boolean
b1=True
print(b1)
print(type(b1))
b2=False
print(b2)
print(type(b2))

#none type
n=None
print(n)
print(type(n))
