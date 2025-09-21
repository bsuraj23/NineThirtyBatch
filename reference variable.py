# reference variable   
class sample():
    a=30
    b=40
    
kee=sample()

srii=kee
print(srii.b)
print(kee.a)
print(srii.b)
print(id(kee))
print(id(srii))
srii.a=100
print(kee.a)
print(srii.a)
